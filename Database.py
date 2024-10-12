import sqlite3
import json

from requests import delete

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS userdata (
        username text NOT NULL UNIQUE,
        password text,
        first_name text,
        last_name text
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS usersecretquestions (
        SecQue1 text,
        AnswSQ1 text,
        SecQue2 text,
        AnswSQ2 text
    )""")

# null, integer, real, text, blob

def startDB():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

def deleteTable(table):
    c.execute(f"DROP TABLE {table}")

def createUser(username, password, first_name, last_name):
    try:
        c.execute(f"INSERT INTO userdata VALUES ('{username}','{password}','{first_name}','{last_name}')")
    except sqlite3.IntegrityError as e:
        print(f'a constraint failed {e}')

def createUserSQ(SQ1, SQA1, SQ2, SQA2):
    try:
        c.execute(f"INSERT INTO usersecretquestions VALUES ('{SQ1}','{SQA1}','{SQ2}','{SQA2}')")
    except sqlite3.IntegrityError as e:
        print(f'a constraint failed {e}')

def getData():
    c.execute("SELECT * FROM userdata")
    return c.fetchall()

def finDB():
    conn.commit()
    conn.close()
    return

def commitDB():
    conn.commit()

def list_to_string(lst):
    return json.dumps(lst)

def string_to_list(string):
    return json.loads(string)

#deleteTable("userdata")