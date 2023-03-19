import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS users")
    #cur.execute("""CREATE TABLE IF NOT EXISTS users (
     #           name TEXT,
     #           sex TEXT,
      #          old INTEGER,
      #          score INTEGER
     #           )
      #          """)
