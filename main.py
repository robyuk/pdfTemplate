from fpdf import FPDF
import pandas as pd

if __name__ == '__main__':
    pdf = FPDF(orientation='p', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False)
    df = pd.read_csv('topics.csv')

    for index, row in df.iterrows():
        pdf.add_page()
        pdf.set_font(family='Arial', style='B', size=12)
        pdf.set_text_color(80, 80, 240)
        pdf.cell(w=0, h=12, align='l', ln=1, txt=row.Topic)
        pdf.line(x1=11, y1=18, x2=200, y2=18)

        # Footer
        pdf.ln(265)
        pdf.set_font(family='Arial', style='I', size=10)
        pdf.cell(w=0, h=10, align='R', txt=row.Topic)

        for page in range(1, row.Pages):
            pdf.add_page()
            # Footer
            pdf.ln(277)
            pdf.cell(w=0, h=10, align='R', txt=row.Topic)

    pdf.output('output.pdf')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
