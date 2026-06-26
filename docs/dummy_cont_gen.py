import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT

def create_contract_pdf(filename="employment_contract.pdf"):
    # Target Document Setup
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=54,  # 0.75 inch margins
        leftMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Clean Typography Styles
    title_style = ParagraphStyle(
        'ContractTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        spaceAfter=15
    )
    
    subtitle_style = ParagraphStyle(
        'ContractSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=11,
        leading=14,
        alignment=TA_CENTER,
        spaceAfter=25
    )
    
    heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'ContractBody',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=15,
        alignment=TA_JUSTIFY,
        spaceAfter=10
    )
    
    sign_style = ParagraphStyle(
        'SignatureText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        alignment=TA_LEFT
    )

    story = []

    # Title & Metadata
    story.append(Paragraph("EMPLOYMENT AGREEMENT & JOB CONFIRMATION", title_style))
    story.append(Paragraph("This document constitutes a binding legal framework between employee and employer.", subtitle_style))
    
    story.append(HRFlowable(width="100%", thickness=1, color="black", spaceAfter=20))
    
    # Preamble
    preamble_text = (
        "This Employment Agreement (the \"Agreement\") is executed and made effective as of June 26, 2026, "
        "by and between <b>Rista.ai</b> (hereinafter referred to as the \"Company\"), and <b>John Dee</b> "
        "(hereinafter referred to as the \"Employee\")."
    )
    story.append(Paragraph(preamble_text, body_style))
    story.append(Spacer(1, 10))
    
    # Section 1
    story.append(Paragraph("1. Position and Duties", heading_style))
    sec1_text = (
        "The Company hereby confirms the employment of the Employee in the position of <b>Software Engineer</b>. "
        "The Employee agrees to perform the duties, responsibilities, and functions reasonably assigned by the leadership "
        "of Rista.ai. The Employee promises to perform all duties faithfully, safely, and to the absolute best of their professional abilities."
    )
    story.append(Paragraph(sec1_text, body_style))
    
    # Section 2
    story.append(Paragraph("2. Term of Employment", heading_style))
    sec2_text = (
        "Employment shall commence on a mutually agreed date and shall continue until terminated by either party in accordance "
        "with the guidelines laid out within the corporate policy guidelines of the Company."
    )
    story.append(Paragraph(sec2_text, body_style))
    
    # Section 3
    story.append(Paragraph("3. Compensation and Benefits", heading_style))
    sec3_text = (
        "In consideration for the services rendered by the Employee, the Company shall provide a competitive baseline monetary "
        "compensation package, subject to standard deductions and statutory withholdings as mandated by regional legislative rules."
    )
    story.append(Paragraph(sec3_text, body_style))
    
    # Section 4
    story.append(Paragraph("4. Confidentiality & Non-Disclosure", heading_style))
    sec4_text = (
        "The Employee recognizes that during the course of employment, they will have access to proprietary intellectual property, "
        "source code architectures, data configurations, and core operational models belonging to Rista.ai. The Employee agrees to "
        "maintain absolute confidentiality regarding all such information and explicitly notes that any disclosure breach will trigger immediate termination."
    )
    story.append(Paragraph(sec4_text, body_style))
    
    story.append(Spacer(1, 40))
    story.append(Paragraph("IN WITNESS WHEREOF, the parties hereto have executed this Agreement.", body_style))
    story.append(Spacer(1, 30))
    
    # Signatures Structure Layout (Simulated structural spacing)
    sig_block_1 = (
        "<b>For Rista.ai:</b><br/><br/><br/>"
        "___________________________<br/>"
        "Authorized Human Resources Representative<br/>"
        "Date: June 26, 2026"
    )
    
    sig_block_2 = (
        "<b>For the Employee:</b><br/><br/><br/>"
        "___________________________<br/>"
        "John Dee<br/>"
        "Date: June 26, 2026"
    )
    
    story.append(Paragraph(sig_block_1, sign_style))
    story.append(Spacer(1, 40))
    story.append(Paragraph(sig_block_2, sign_style))

    # Build the document
    doc.build(story)
    print(f"Success! '{filename}' has been generated inside your current directory.")

if __name__ == "__main__":
    create_contract_pdf()