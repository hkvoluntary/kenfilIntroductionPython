import csv
import sqlite3

try:
    db = sqlite3.connect('sample.db')
    cursor = db.cursor()
    
    with open('ticker_data.csv', 'r') as ff:
        fcsv = csv.reader(ff)
    
        # `recs_to_load` is a list of records contained in `ticker_data.csv`.
        recs_to_load = [record for record in fcsv]

        # Call `cursor.executemany`, specifying `recs_to_load`.
        cursor.executemany("INSERT INTO CLOSING_PRICES VALUES (?,?,?)", recs_to_load)
finally:
    db.commit()
    db.close()