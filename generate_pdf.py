import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

pdf_filename = "PocketSmart_AI_Project_Report.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)

styles = getSampleStyleSheet()
story = []

# Title & Custom Styles
title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=20, textColor=colors.HexColor('#0D9488'), alignment=1, spaceAfter=15)
section_style = ParagraphStyle('SectionStyle', parent=styles['Heading2'], fontSize=13, textColor=colors.HexColor('#0F766E'), spaceBefore=12, spaceAfter=6)
body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=9.5, leading=13, textColor=colors.HexColor('#1F2937'), spaceAfter=6)

# Title
story.append(Paragraph("<b>POCKETSMART AI: BUDGET & RECOMMENDATION ASSISTANT</b>", title_style))
story.append(Spacer(1, 10))

# Abstract
abstract_text = """<b>1. ABSTRACT</b><br/>
PocketSmart AI is an intelligent budget allocation and product recommendation web application built with Streamlit and Gemini AI. It provides customized financial and shopping plans across Home Interiors, Party Events, and Jewelry purchases."""
story.append(Paragraph(abstract_text, body_style))
story.append(Spacer(1, 8))

# Problem Statement
problem_text = """<b>2. PROBLEM STATEMENT</b><br/>
Planning event or purchase budgets often leads to overspending due to lack of structured estimates and personalized product suggestions. PocketSmart AI solves this by dynamically calculating itemized budget splits based on user parameters."""
story.append(Paragraph(problem_text, body_style))
story.append(Spacer(1, 8))

# Key Modules & Features
features_text = """<b>3. KEY MODULES & TECH STACK</b><br/>
* <b>Home Interior Planner:</b> Room-wise budget allocation & item recommendations.<br/>
* <b>Party Budget Planner:</b> Guest count & event based expense distribution.<br/>
* <b>Jewelry Planner:</b> Metal preference and occasion based budget guide.<br/>
* <b>Tech Stack:</b> Python 3.12, Streamlit UI, Google Gemini API (google-generativeai), ReportLab."""
story.append(Paragraph(features_text, body_style))
story.append(Spacer(1, 10))

# Screenshots Section
story.append(Paragraph("<b>4. PROJECT SCREENSHOTS & PROOF OF WORK</b>", section_style))

image_files = ["pocket1.jpg", "pocket2.jpg", "pocket3.jpg"]

for img_name in image_files:
    if os.path.exists(img_name):
        try:
            story.append(Image(img_name, width=420, height=210))
            story.append(Spacer(1, 10))
        except Exception as e:
            story.append(Paragraph(f"<i>[Image {img_name} loading error: {e}]</i>", body_style))
    else:
        story.append(Paragraph(f"<i>[Image {img_name} not found in folder]</i>", body_style))

doc.build(story)
print("SUCCESS: PDF created as PocketSmart_AI_Project_Report.pdf!")