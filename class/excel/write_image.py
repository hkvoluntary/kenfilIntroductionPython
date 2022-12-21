from openpyxl import Workbook
from openpyxl.drawing.image import Image

book = Workbook()
sheet = book.active

img = Image("happy.jfif")
sheet['A1'] = 'This is Sid'

sheet.add_image(img, 'B2')

book.save("sheet_image.xlsx")