from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from datetime import datetime
import os

def generate_pdf(analysis_data, filename, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#00c9a7'),
        spaceAfter=30,
        alignment=1
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#1a2333'),
        spaceAfter=12
    )
    
    story.append(Paragraph("Medical Report Analysis", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    info_data = [
        ['Report Name:', filename],
        ['Analysis Date:', datetime.now().strftime('%d %B %Y')],
        ['Health Score:', f"{analysis_data['health_score']}/100"]
    ]
    
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f4f9')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    
    story.append(info_table)
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("Summary", heading_style))
    story.append(Paragraph(analysis_data['summary'], styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    if analysis_data.get('issues'):
        story.append(Paragraph("Issues Detected", heading_style))
        
        issue_data = [['Parameter', 'Value', 'Status', 'Deviation']]
        for issue in analysis_data['issues']:
            issue_data.append([
                issue['name'],
                f"{issue['value']} {issue['unit']}",
                issue['status'],
                f"{issue['deviation']}%"
            ])
        
        issue_table = Table(issue_data, colWidths=[2*inch, 1.5*inch, 1.5*inch, 1*inch])
        issue_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#00c9a7')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(issue_table)
        story.append(Spacer(1, 0.2*inch))
    
    if analysis_data.get('patterns'):
        story.append(PageBreak())
        story.append(Paragraph("Pattern Analysis", heading_style))
        
        for pattern in analysis_data['patterns']:
            story.append(Paragraph(f"<b>{pattern['name']}</b>", styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
            story.append(Paragraph(pattern['explanation'], styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
            story.append(Paragraph("<b>Action Required:</b>", styles['Normal']))
            story.append(Paragraph(pattern['action'], styles['Normal']))
            story.append(Spacer(1, 0.2*inch))
    
    story.append(PageBreak())
    story.append(Paragraph("Final Advice", heading_style))
    story.append(Paragraph(analysis_data['final_advice'], styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    disclaimer_style = ParagraphStyle(
        'Disclaimer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        alignment=1
    )
    
    story.append(Paragraph(
        "This report is AI-generated and for informational purposes only. "
        "Please consult a qualified medical professional for diagnosis and treatment.",
        disclaimer_style
    ))
    
    doc.build(story)
    return output_path
