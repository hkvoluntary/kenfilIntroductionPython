
import sqlite3

try:
    db = sqlite3.connect("sample.db")
    cursor = db.cursor()
    params = {'symbol':'GE', 'date':'20161125'}
    SQL = "SELECT * FROM CLOSING_PRICES WHERE TICKER=:symbol AND DATE!=:date"
    cursor.execute(SQL, params)
    headers = [i[0] for i in cursor.description]
    print(headers)

    for rec in cursor:
        print(rec)
        


finally:

    db.close()



