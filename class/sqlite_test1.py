import sqlite3

# Create new database `sample.db`. Notice `sample.db` is now 
# listed in your working directory.
db = sqlite3.connect("sample.db")

# Initiate a cursor, and call the connection's cursor method.
cursor = db.cursor()

# Specify the DDL to create the two tables:
tbl1_ddl = """CREATE TABLE CLOSING_PRICES (
              DATE   TEXT,
              TICKER TEXT,
              CLOSE  REAL)"""

tbl2_ddl = """CREATE TABLE TICKER_MAPPING (
              TICKER       TEXT,
              COMPANY_NAME TEXT)"""

# Call the `cursor.execute` method, passing tbl1_ddl & tbl2_ddl as arguments.
cursor.execute(tbl1_ddl)
cursor.execute(tbl2_ddl)

# IMPORTANT! Be sure to commit changes you want to persist. Without
# commiting, changes will not be saved.
db.commit()

# Close connection to `sample.db`.
db.close()