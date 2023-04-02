import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
               name TEXT NOT NULL,
               sex TEXT,
               old INTEGER DEFAULT 18,
               score INTEGER DEFAULT 0
               )
              """)
    
    cur.execute("""INSERT INTO users VALUES (
                'Михаил',
                'муж',
                19,
                1000
                )
                """)
    
    cur.execute("""INSERT INTO users VALUES (
                'Cаша',
                'жен',
                20,
                1500
                )
                """)
    
    cur.execute("SELECT * FROM users")

    result = cur.fetchall()
    print(result)

    

    

