import sqlite3
from openpyxl import Workbook

book = Workbook()
sheet = book.active

try:
    db = sqlite3.connect('sample.db')
    cursor = db.cursor()

    # Query to select all records from `CLOSING_PRICES`:
    SQL = "SELECT * FROM CLOSING_PRICES"

    cursor.execute(SQL)
    values = []
    print(cursor)
    print(type(cursor))

    # Iterate over cursor to print records. 
    for rec in cursor:
        print(rec)
        values.append(rec)


    def myFunc(e):
        return e[1]

    print("before sort:", values)
    values.sort(key=myFunc)
    print("after sort", values)

    for item in values:
        sheet.append(item)

finally:
    db.close()


book.save("sqlite_test.xlsx")