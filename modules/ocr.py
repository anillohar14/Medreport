import cv2
import os
import uuid
import pytesseract
from pdf2image import convert_from_path


# ─────────────────────────────────────────────────────────────
# SETTINGS
# ─────────────────────────────────────────────────────────────

import shutil
POPPLER_PATH = shutil.which('pdftoimage') or None

PDF_DPI = 300

MIN_TEXT_LENGTH = 50


# ─────────────────────────────────────────────────────────────
# IMAGE PREPROCESSING
# ─────────────────────────────────────────────────────────────

def preprocess_standard(img):
    """
    Standard preprocessing — zyaadatar cases mein kaam karta hai.
    Steps: resize → grayscale → blur → threshold
    """
    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 3)

    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    return thresh


def preprocess_adaptive(img):
    """
    Adaptive preprocessing — uneven lighting wali images ke liye.
    Jab normal threshold fail kare tab ye try karo.
    """
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    gray = clahe.apply(gray)

    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    return thresh


# ─────────────────────────────────────────────────────────────
# OCR FROM IMAGE
# ─────────────────────────────────────────────────────────────

def extract_text_from_image(image_path):

    img = cv2.imread(image_path)
    if img is None:
        print(f"  [OCR] ERROR: Image nahi padh saka — {image_path}")
        return ""

    processed = preprocess_standard(img)

    custom_config = (
        r'--oem 3 --psm 6 '
        r'-c tessedit_char_whitelist='
        r'0123456789.%abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ: '
    )

    text = pytesseract.image_to_string(processed, config=custom_config)

    if len(text.strip()) < MIN_TEXT_LENGTH:
        print(f"  [OCR] Standard preprocessing ne sirf {len(text.strip())} chars diye — adaptive try kar raha hun...")

        processed_alt = preprocess_adaptive(img)
        text_alt = pytesseract.image_to_string(processed_alt, config=custom_config)

        if len(text_alt.strip()) > len(text.strip()):
            print(f"  [OCR] Adaptive better result diya: {len(text_alt.strip())} chars")
            text = text_alt
        else:
            print(f"  [OCR] Standard hi better tha — usse rakh raha hun")

    return text


# ─────────────────────────────────────────────────────────────
# OCR FROM PDF
# ─────────────────────────────────────────────────────────────

def extract_text_from_pdf(pdf_path):
    """
    PDF ke har page se text nikalo.
    Har page → temp image → OCR → text jodo.
    Temp files guaranteed delete hongi — error ho ya na ho.
    """
    print(f"[OCR] PDF processing shuru: {os.path.basename(pdf_path)}")

    try:
        pages = convert_from_path(
            pdf_path,
            dpi=PDF_DPI,
            poppler_path=POPPLER_PATH
        )
    except Exception as e:
        print(f"[OCR] ERROR: PDF pages convert nahi ho sake — {e}")
        print("[OCR] Hint: Poppler install hai? POPPLER_PATH set karo file mein.")
        return ""

    print(f"[OCR] {len(pages)} pages mile — ab har page padhenge...")

    full_text = ""

    for i, page in enumerate(pages):
        temp_path = f"_ocr_temp_page_{uuid.uuid4().hex}_{i}.jpg"
        page_num  = i + 1

        try:
            page.save(temp_path, "JPEG")
            print(f"  [OCR] Page {page_num}/{len(pages)} process ho raha hai...")

            page_text = extract_text_from_image(temp_path)

            if not page_text.strip():
                print(f"  [OCR] WARNING: Page {page_num} se koi text nahi mila!")
            else:
                char_count = len(page_text.strip())
                print(f"  [OCR] Page {page_num} done — {char_count} characters mile")

            full_text += page_text + "\n"

        except Exception as e:
            print(f"  [OCR] ERROR: Page {page_num} process nahi ho saka — {e}")
            continue

        finally:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except Exception as del_err:
                    print(f"  [OCR] WARNING: Temp file delete nahi hui — {del_err}")

    total_chars = len(full_text.strip())
    print(f"[OCR] Completed — Total: {total_chars} characters extracted")

    if total_chars < MIN_TEXT_LENGTH:
        print("[OCR] WARNING: Bahut kam text mila! PDF theek se scan hua hai?")

    return full_text


# ─────────────────────────────────────────────────────────────
# MAIN FUNCTION
# ─────────────────────────────────────────────────────────────

def extract_text(file_path):
    """
    Smart entry point.
    PDF hai → extract_text_from_pdf()
    Image hai → extract_text_from_image()
    """
    ext = file_path.lower()

    if ext.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif ext.endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif")):
        print(f"[OCR] Image processing: {os.path.basename(file_path)}")
        text = extract_text_from_image(file_path)
        print(f"[OCR] Done — {len(text.strip())} characters mile")
        return text

    else:
        print(f"[OCR] WARNING: Unknown file type — try kar raha hun as image")
        return extract_text_from_image(file_path)


# ─────────────────────────────────────────────────────────────
# QUICK TEST
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python ocr.py <file_path>")
        print("Example: python ocr.py samples/report.pdf")
        sys.exit(1)

    path = sys.argv[1]

    if not os.path.exists(path):
        print(f"ERROR: File nahi mili — {path}")
        sys.exit(1)

    print("=" * 50)
    result = extract_text(path)
    print("=" * 50)
    print("\n--- OCR OUTPUT (pehle 1000 chars) ---")
    print(result[:1000])
    print(f"\n--- Total: {len(result)} characters ---")
