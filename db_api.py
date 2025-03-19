" database stuff for the vulnerable server "

import sqlite3 # thank the standard library!

DATABASE_LOCATION = "users.db"
DEFAULT_DATA = [ # in (username, password, balance) format
    ("elon", '$paceX69', 232942756104),
    ("hacker", "crAzyStr0ngPassWord", 42),
]

def build_database(database: str=DATABASE_LOCATION,
                   data: list[tuple[str, str, int]]=DEFAULT_DATA) -> sqlite.Connection:
    " build the default credential database to hack into and return a connection to it "
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("CREATE TABLE users(username, password, balance)")
    curs.executemany("INSERT INTO users(?,?,?)", data)
    conn.commit()

    return conn
