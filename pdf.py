from fpdf import FPDF


def add_txt_to_pdf(pdf, txt="", font_family='Arial', font_style='', font_size=16, alignment='L',
                   fill=False, link='', border=0, new_line=1, cell_width=0,  # 0 takes the whole line
                   cell_height=10):
    if pdf:
        pdf.set_font(font_family, font_style, font_size)
        pdf.cell(cell_width, cell_height, txt, border, new_line, alignment, fill, link)
    else:
        print("Invalid pdf!")


def add_img_to_pdf(pdf, imgPath, pos_x=0, pos_y=0, width=0, height=0):
    # width, height = 0 means auto
    pdf.image(imgPath, pos_x, pos_y, width, height)


def draw_line(pdf, x1, y1, x2, y2):
    pdf.line(x1, y1, x2, y2)


def new_pdf():
    pdf = FPDF('P', 'mm', (40, 40))

    pdf.add_page()
    add_img_to_pdf(pdf, "ean.png", 0, 0, 5, 5)
    pdf.set_x(0)
    pdf.set_y(35)
    add_txt_to_pdf(pdf, "some txt", cell_width=50, cell_height=10, border=1)
    add_img_to_pdf(pdf, "ean1.png", 0, 50, 75, 30)
    draw_line(pdf, 0, 30, 0, 50)

    pdf.output('my_pdf.pdf', 'F')


new_pdf()
