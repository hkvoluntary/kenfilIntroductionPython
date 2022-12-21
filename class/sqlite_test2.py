import sqlite3

db = sqlite3.connect('sample.db')
cursor = db.cursor()

cursor.execute("INSERT INTO TICKER_MAPPING VALUES ('AXP',  'American Express Company')")
cursor.execute("INSERT INTO TICKER_MAPPING VALUES ('GE' ,  'General Electric Company')")
cursor.execute("INSERT INTO TICKER_MAPPING VALUES ('GS' ,  'Goldman Sachs Group Inc')")
cursor.execute("INSERT INTO TICKER_MAPPING VALUES ('UTX' , 'United Technologies Corporation')")

closing_prices = [
    ('20160722', 'AXP',  64.28), ('20160722', 'GE' ,  32.06),
    ('20160722', 'GS' , 160.41), ('20160722', 'UTX', 105.13)
    ]
    
cursor.executemany("INSERT INTO CLOSING_PRICES VALUES (?,?,?)", closing_prices)

db.commit()
db.close()




