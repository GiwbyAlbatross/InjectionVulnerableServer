" database stuff for the vulnerable server "

import os
import secrets
import sqlite3 # thank the standard library!

DATABASE_LOCATION = "users.db"
DEFAULT_DATA = [ # in (username, password, balance, authId) format
    ("elon", '$paceX69', 232942756104, -1),
    ("hacker", "crAzyStr0ngPassWord", 42, -1),
]

def build_database(database: str=DATABASE_LOCATION,
                   data: list[tuple[str, str, int]]=DEFAULT_DATA) -> sqlite3.Connection:
    " build the default credential database to hack into and return a connection to it "
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    curs.execute("CREATE TABLE users(username, password, balance)")
    curs.executemany("INSERT INTO users(?,?,?,?)", data)
    conn.commit()

    return conn

def authenticate_user(name: str, password: str, conn: sqlite3.Connection) -> int:
    " really bad authentication which is vulnerable to all kinds of attacks, from SQL injection, to just leaking the database "
    with open(os.path.join('sql-templates', 'auth.sql')) as f:
        query = f.read()
    curs = conn.cursor()
    res = curs.execute(query.format(name, password))
    if res.fetchone() is not None: # if the returned username from the SQL code isn't NULL, basically
        authId = secrets.randbits(384)
    else:
        authId = -1 # -1 means 'not logged in anywhere'
    with open(os.path.join('sql-templates', 'authId-update.sql')) as f:
        query = f.read()
    curs.execute(query.format(name, authId))
    conn.commit()
    return authId

def is_user_logged_in(name: str, authId: int, conn: sqlite3.Connection) -> bool:
    curs = conn.cursor()
    with open(os.path.join('sql-templates', 'is_authenticated.sql')) as f:
        query = f.read()
    res = curs.execute(query.format(name))
    return res.fetchone() == authId

def log_out_user(name: str, conn: sqlite3.Connection) -> int:
    " log out a user `name` using `conn`. Return the new authId "
    with open(os.path.join('sql-templates', 'authId-update.sql')) as f:
        query = f.read()
    authId = -1
    curs = conn.cursor()
    curs.execute(query.format(name, authId))
    conn.commit()
    return authId
