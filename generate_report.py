from reportlab.platypus import LongTable, TableStyle
from reportlab.lib import colors
from reportlab.platypus.flowables import Spacer
from reportlab.pdfgen import canvas

def create_table(table_data):
    colwidths = (70, 50, 50, 50, 50, 50)
    rowheights = (25, 20, 20)
    table = LongTable(table_data, colWidths=colwidths, rowHeights=rowheights,hAlign="LEFT")
    table_style = TableStyle(
        [
            ('GRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black)
            ('ALIGN', (1, 1), (-1, -1), 'LEFT'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('FONT', (0, 0), (0, -1), 'Times-Bold'), # Set header text to bold
            ('FONT', (1, 0), (-1, -1), 'Times-Roman')
        ]
    )
    table.setStyle(table_style)
    return table

canva = canvas.Canvas("test.pdf")
fonts = canva.getAvailableFonts()
print(help(colors))
print(fonts)
['Courier', 'Courier-Bold', 'Courier-BoldOblique', 'Courier-Oblique', 'Helvetica', 'Helvetica-Bold', 'Helvetica-BoldOblique', 'Helvetica-Oblique',
 'Symbol', 'Times-Bold', 'Times-BoldItalic', 'Times-Italic', 'Times-Roman', 'ZapfDingbats']