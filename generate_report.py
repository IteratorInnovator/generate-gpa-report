from reportlab.platypus import LongTable, TableStyle, Paragraph, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.platypus.flowables import Spacer
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from process_data import load_json


def create_table(table_data):
    colwidths = (70, 50, 50, 50, 50, 50)
    rowheights = (25, 20, 20)
    table = LongTable(table_data, colWidths=colwidths, rowHeights=rowheights,hAlign="LEFT")
    table_style = TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (1, 1), (-1, -1), 'LEFT'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('FONT', (0, 0), (0, -1), 'Times-Bold'), # Set header text to bold
            ('FONT', (1, 0), (-1, -1), 'Times-Roman'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0.25)
        ]
    )
    table.setStyle(table_style)
    return table

def create_semester_header(semester):
    header_text = f"""
    <font name=Times color={colors.black} size=12><u>{semester}</u></font>
    """
    header_style = ParagraphStyle()
    header = Paragraph(text=header_text)
    return header

def create_total_summary(semester_total):
    text = f"""
    <font name=Times color={colors.black} size=12>
        <p>Course units earned: {semester_total[1]}/4.0</p>
        <p>Semester GPA: {semester_total[0]:.2f}/4.0</p>
    </font>
    """
    text_style = ParagraphStyle(fontName='Times', fontSize=12)
    total_summary_text = Paragraph(text=text, style=text_style)
    
def create_cumulative_summary(CGPA, total_credit_units_earned):
    summary_text = f"""
    <font name=Times color={colors.black} size=12>
        <p><u>Cumulative Total</u></p>
        <p>Course Units Earned = {total_credit_units_earned}</p>_
        <p>Cumulative CPA = {CGPA}</p>
    </font>
    """
    text_style = ParagraphStyle(fontName='Times', fontSize=12)
    cumulative_summary = Paragraph(text=summary_text, style=text_style)
    return cumulative_summary

def create_pdf_title(JSON_FIlE):
    student_info_dict = load_json(JSON_FIlE)
    student_name = student_info_dict["name"]
    date_of_birth = student_info_dict["date_of_birth"]
    date_of_enrolment = student_info_dict["date_of_enrolment"]
    student_id = student_info_dict["student_ID"]
    title_text = f"""
    <section>
        <font name=Times size=14>
            <p><b><u>Singapore Management University</u></b></p>
        </font>
    </section>
    """
    pdf_title = Paragraph()
    
    
print(help(Paragraph))
# canva = canvas.Canvas("test.pdf")
# fonts = canva.getAvailableFonts()
# print(help(colors))
# print(fonts)
# ['Courier', 'Courier-Bold', 'Courier-BoldOblique', 'Courier-Oblique', 'Helvetica', 'Helvetica-Bold', 'Helvetica-BoldOblique', 'Helvetica-Oblique',
#  'Symbol', 'Times-Bold', 'Times-BoldItalic', 'Times-Italic', 'Times-Roman', 'ZapfDingbats']