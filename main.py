from fpdf import FPDF
import glob
import pandas as pd
from pathlib import Path

filepaths = glob.glob('Excel_Files/*.xlsx')

for file_path in filepaths:
    print(file_path)
    df = pd.read_excel(file_path, sheet_name='Sheet 1')
    print(df)

    pdf = FPDF(orientation='p',unit='mm',format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', style='b', size=16)
    file_name = Path(file_path).stem
    invoice_name, Date = file_name.split('-')
    pdf.cell(w=50, h=8, txt=f'Invoice no. {invoice_name}', align='L', ln=1)


    invoice_name = file_name.split('-')[1]
    pdf.cell(w=50, h=8, txt=f'Date {Date}', align='L', ln=1)

    pdf.output(f'PDFS/{file_name}.pdf')
    # print(invoice_name)


# pdf.set_auto_page_break(auto=False,margin=0)
#
# df = pd.read_csv('topics.csv')
# for index, row in df.iterrows():
#     for page_num in range(row['Pages']-1):
#         pdf.add_page()
#         pdf.set_font(family='Times', style='b', size=24)
#         pdf.set_text_color(100, 100, 100)
#         pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
#         pdf.line(10,22,200,22)
#
#
#         pdf.ln(265)
#         pdf.set_font(family='Times', style='b', size=10)
#         pdf.set_text_color(150, 150, 150)
#         pdf.cell(w=0, h=12, txt=row['Topic'], align='R', ln=1)