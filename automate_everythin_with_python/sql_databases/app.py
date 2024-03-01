import sqlite3
import csv
import pandas
from fpdf import FPDF

connection = sqlite3.connect("database.db")

SELECT_ALL = "Select * from 'ips' ORDER BY asn"
cursor = connection.cursor()
cursor.execute(SELECT_ALL)
all_info = cursor.fetchall()

# using csv
with open("sql_to_csv.csv", mode="w", encoding="utf-8") as transformation:
    writer = csv.writer(transformation)
    writer.writerows(all_info)

# using pandas
df = pandas.read_sql_query(SELECT_ALL, connection)
df.to_csv(path_or_buf="database.csv", index=False)
df.to_excel("database.xlsx", index=False)

# using pdf
cursor.execute("PRAGMA table_info(ips)")
columns_name = cursor.fetchall()
columns = [column[1] for column in columns_name]
pdf = FPDF(orientation="P", unit="pt", format="A4")
pdf.add_page()


for column in columns:
    pdf.set_font(family="Times", style="B", size=14)
    pdf.cell(w=100, h=30, txt=column, border=1)
pdf.ln()

rows = cursor.execute(SELECT_ALL).fetchall()
for row in rows:
    for element in row:
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=30, txt=str(element), border=1)
    pdf.ln()

pdf.output("sql_to_pdf.pdf")

# insert data
new_rows = [
    ("10.0.0.1", "a.b.c", 100),
    ("10.0.0.255", "d.e.f", 100),
]

cursor.executemany("INSERT INTO ips values (?,?,?)", new_rows)
connection.commit()

cursor.execute(SELECT_ALL)
print(cursor.fetchall())
connection.close()
