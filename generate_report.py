from reportlab.platypus import Table, LongTable, TableStyle, Paragraph, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.platypus.flowables import Spacer
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from process_data import load_json, get_current_date


def create_header():
    styles = getSampleStyleSheet()
    header_style = styles["Heading1"]
    header_style.alignment = 1
    header_style.fontName = "Times-Bold"
    header_style.fontSize = 14
    header = Paragraph("<u>Singapore Management University</u>", style=header_style)
    return header

def create_line_divider():
    horizontal_line = Table([""], colWidths=570)
    horizontal_line.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 1, colors.black)
    ]))
    return horizontal_line

def create_student_info_section(JSON_FIlE):
    student_info_dict = load_json(JSON_FIlE)
    student_name = student_info_dict["name"]
    date_of_birth = student_info_dict["date_of_birth"]
    date_of_enrolment = student_info_dict["date_of_enrolment"]
    student_id = student_info_dict["student_ID"]
    left_section_text = f"""
    <p>
        Name: {student_name}<br/>
        Date of Enrolment: {date_of_enrolment}<br/>
        Date of Birth: {date_of_birth}<br/>
    </p>
    """
    right_section_text = f"""
    <p>
        Student ID: {student_id}<br/>
        Date of Issue: {get_current_date()}<br/>
    </p>
    """
    section_style = ParagraphStyle(
        name="section style",
        alignment=0,
        fontName="Times-Roman",
        fontSize=10
    )
    left_section = Paragraph(text=left_section_text, style=section_style)
    right_section = Paragraph(text=right_section_text, style=section_style)
    section_table = Table([[left_section, "", right_section]], colWidths=190)
    section_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (0,0), (0,0), 'LEFT'),
        ('ALIGN', (0,1), (0,1), 'RIGHT'),
    ]))
    return section_table


def create_table(table_data):
    colwidths = [None] * len(table_data[0]) # Dynamically adjust column widths
    rowheights = [18 for row in table_data]
    table = LongTable(table_data, colWidths=colwidths, rowHeights=rowheights,hAlign="LEFT")
    table_style = TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'), # Center all data in cells
            ('ALIGN', (0, 0), (0, -1), 'LEFT'), # Align course column to left
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('FONT', (0, 0), (-1, 0), 'Times-Bold'), # Set header row to bold
            ('FONT', (0, 1), (-1, -1), 'Times-Roman'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0.25)
        ]
    )
    table.setStyle(table_style)
    return table

def create_semester_header(semester):
    header_text = f"""
        <p>
            <b><u>{semester["semester"]}</u></b><br/>
            Start date: {semester["start_date"]}<br/>
            End date: {semester["end_date"]}<br/>
    """
    header_style = ParagraphStyle(name="style", fontName="Times", fontSize=10)
    header = Paragraph(text=header_text, style=header_style)
    return header


def create_total_summary(semester_total):
    summary_text = f"""
    <p>
        Course units earned: {semester_total[1]}/{semester_total[2]}<br/>
        Semester GPA: {semester_total[0]:.2f}/4.0<br/>
    </p>
    """
    text_style = ParagraphStyle(name="style", fontName='Times', fontSize=10, alignment=2)
    total_summary = Paragraph(text=summary_text, style=text_style)
    return total_summary
   
    
def create_cumulative_summary(CGPA, total_credit_units_earned, total_credit_units_attempted):
    summary_text = f"""
    <p>
        <u><b>Cumulative Total</b></u><br/>
        Course Units Attempted = {total_credit_units_attempted}<br/>
        Course Units Earned = {total_credit_units_earned}<br/>
        Cumulative CPA = {CGPA}<br/>
    </p>
    """
    text_style = ParagraphStyle(name="style", fontName='Times', fontSize=11, alignment=0)
    cumulative_summary = Paragraph(text=summary_text, style=text_style)
    return cumulative_summary