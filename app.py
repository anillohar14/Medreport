from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_file
import os
import tempfile
from functools import wraps
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__, 
            template_folder='web/templates', 
            static_folder='web/static')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['REPORT_FOLDER'] = 'reports'

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['REPORT_FOLDER'], exist_ok=True)

# Import utility modules
from modules.lang_utils import t, normalise_lang
from database import init_db, create_user, verify_user, save_report, get_user_reports, get_report_data
from modules.pdf_generator import generate_pdf

# Supported languages: English, Hindi (Devanagari), Hinglish (Roman Hindi)
ALL_LANGS = ('en', 'hi', 'hin')

# ============================================================================
# AUTHENTICATION DECORATOR
# ============================================================================
def login_required(f):
    """
    Decorator to protect routes that require authentication.
    If user is not logged in, redirect to login page.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = verify_user(username, password)
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return jsonify({'success': True, 'redirect': url_for('dashboard')})
        else:
            return jsonify({'success': False, 'error': 'Invalid credentials'})
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        success, message = create_user(username, email, password)
        if success:
            return jsonify({'success': True, 'message': message})
        else:
            return jsonify({'success': False, 'error': message})
    
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    reports = get_user_reports(session['user_id'])
    return render_template('dashboard.html', 
                         username=session['username'], 
                         reports=reports)

@app.route('/analyze')
@login_required
def analyze_page():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
@login_required
def analyze_report():
    lang = normalise_lang(request.form.get('lang', 'en'))
    
    if 'file' not in request.files:
        return jsonify({'error': t('err_no_file', lang)}), 400
    
    file = request.files['file']
    if not file or file.filename == '':
        return jsonify({'error': t('err_no_select', lang)}), 400
    
    filename = secure_filename(file.filename)
    ext = os.path.splitext(filename)[1].lower() or '.pdf'
    tmp_fd, tmp_path = tempfile.mkstemp(suffix=ext)
    os.close(tmp_fd)
    
    try:
        file.save(tmp_path)
        text = _smart_extract(tmp_path)
        
        from modules.extractor import extract_values
        data, _ = extract_values(text, debug=False)
        
        if not data:
            return jsonify({'error': t('err_no_values', lang)}), 422
        
        from modules.analyzer import analyze
        all_langs_result = {}
        for lg in ALL_LANGS:
            r = analyze(data, lang=lg)
            all_langs_result[lg] = {
                'summary': r['summary'],
                'health_score': int(r['health_score']),
                'score_label': r['score_label'],
                'score_color': r['score_color'],
                'issues': r['issues'],
                'borderline': r['borderline'],
                'normal': r['normal'],
                'by_category': r['by_category'],
                'patterns': r['patterns'],
                'final_advice': r['final_advice'],
                'total_checked': r['total_checked'],
            }
        
        report_id = save_report(
            session['user_id'],
            filename,
            all_langs_result,
            all_langs_result['hin']['health_score']
        )
        
        return jsonify({
            'success': True, 
            'all_langs': all_langs_result,
            'report_id': report_id
        })
    
    except Exception as e:
        import traceback
        error_msg = str(e)
        print(traceback.format_exc())
        if "tesseract is not installed" in error_msg.lower() or "tesseractnotfounderror" in str(type(e)).lower():
            friendly_err = "OCR component (Tesseract) is missing on the server. Please ensure the app is deployed using Docker on Render."
        elif "libgl.so.1" in error_msg.lower():
            friendly_err = "OpenCV dependency missing. Deployment environment is incorrect."
        else:
            friendly_err = f"An unexpected error occurred: {error_msg}"
        return jsonify({'error': friendly_err}), 500
    
    finally:
        try:
            os.unlink(tmp_path)
        except:
            pass

@app.route('/report/<int:report_id>')
@login_required
def view_report(report_id):
    report_data = get_report_data(report_id, session['user_id'])
    if not report_data:
        return "Report not found", 404
    
    return jsonify({'success': True, 'all_langs': report_data})

@app.route('/download/<int:report_id>')
@login_required
def download_report(report_id):
    # Always use Hinglish for PDF download
    lang = 'hin'
        
    report_data = get_report_data(report_id, session['user_id'])
    if not report_data:
        return "Report not found", 404
    
    pdf_filename = f"report_{report_id}_{lang}.pdf"
    pdf_path = os.path.join(app.config['REPORT_FOLDER'], pdf_filename)
    
    generate_pdf(report_data[lang], f"Medical_Report_{report_id}_{lang}", pdf_path)
    
    return send_file(pdf_path, as_attachment=True, 
                    download_name=f"MedReport_{report_id}_{lang}.pdf")

def _smart_extract(file_path):
    if file_path.lower().endswith('.pdf'):
        try:
            import pdfplumber
            text = ''
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    pt = page.extract_text()
                    if pt:
                        text += pt + '\n'
            if len(text.strip()) > 50:
                print(f"Extracted {len(text)} chars using pdfplumber")
                return text
        except ImportError:
            print("pdfplumber not installed, using OCR")
        except Exception as e:
            print(f"pdfplumber error: {e}, using OCR")
    
    print("Using OCR extraction")
    from modules.ocr import extract_text
    return extract_text(file_path)

if __name__ == '__main__':
    init_db()
    
    # Render mein port environment se ata hai
    port = int(os.environ.get('PORT', 5000))
    
    print("\n" + "="*60)
    print("  MedReport - Medical Report Analyzer")
    print(f"  URL: http://localhost:{port}")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=port, debug=False)
