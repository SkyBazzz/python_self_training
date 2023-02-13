"""
Module to create pdf file
also look at:
fitz ro read text from pdf
read tables from pdf tabula-py

import tabula

table = tabula.read_pdf('Table and Text.pdf', pages=1)
table[0].to_excel('output.xlsx', index=None)

"""

from fpdf import FPDF

pdf = FPDF(orientation="p", unit="pt", format="A4")
pdf.add_page()
pdf.image("./resources/afu.svg.png", w=80, h=50)

pdf.set_font(family="Times", style="B", size=24)
pdf.cell(w=0, h=50, txt="Armed Forces of Ukraine", align="C", ln=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=0, h=50, txt="Description", ln=1)

pdf.set_font(family="Times", size=12)

DESCRIPTION = """
The Armed Forces of Ukraine, most commonly known in Ukraine as ZSU or anglicized as AFU,
are the military forces of Ukraine. All military and security forces, including the Armed Forces,
are under the command of the President of Ukraine and subject to oversight by a permanent Verkhovna Rada parliamentary
commission. They trace their lineage to 1917, while the modern armed forces were formed
after Ukrainian independence in 1991.
"""
pdf.multi_cell(w=0, h=15, txt=DESCRIPTION)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100, h=25, txt="Service:")

pdf.set_font(family="Times", size=14)
pdf.cell(w=100, h=25, txt="Army", ln=1)

pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=100, h=25, txt="branches:")

pdf.set_font(family="Times", size=14)
BRANCHES = "Navy Air Force, Air Assault Forces, Special Operations Forces, Territorial Defense Forces"
pdf.multi_cell(w=100, h=25, txt=BRANCHES)

pdf.output("./output/my_pdf.pdf")
