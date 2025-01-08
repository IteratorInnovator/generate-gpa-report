from reportlab.platypus import LongTable, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.platypus.flowables import Spacer
from reportlab.pdfgen import canvas
from reportlab.platypus.paragraph import ParaLines


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
    header = Paragraph(text=header_text)
    return header

def create_total_summary(semester_total):
    text = f"""
    <font name=Times color={colors.black} size=12>
        <p>Course units earned: {semester_total[1]}/4.0</p>
        <p>Semester GPA: {semester_total[0]:.2f}/4.0</p>
    </font>
    """
    total_summary_text = Paragraph(text=text)

print(create_semester_header("2024/2025 Semester 1"))

# canva = canvas.Canvas("test.pdf")
# fonts = canva.getAvailableFonts()
# print(help(colors))
# print(fonts)
# ['Courier', 'Courier-Bold', 'Courier-BoldOblique', 'Courier-Oblique', 'Helvetica', 'Helvetica-Bold', 'Helvetica-BoldOblique', 'Helvetica-Oblique',
#  'Symbol', 'Times-Bold', 'Times-BoldItalic', 'Times-Italic', 'Times-Roman', 'ZapfDingbats']