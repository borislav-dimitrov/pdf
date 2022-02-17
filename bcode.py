import barcode
from barcode.writer import ImageWriter


def create_ean(content, filename="ean"):
    my_bc = barcode.get('ean13', content, writer=ImageWriter())
    my_bc.save(filename)


create_ean("999999999999", "ean1")
