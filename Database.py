import sqlite3
import json

conn = sqlite3.connect('database.db')
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS userdata (
        username text NOT NULL UNIQUE,
        password text,
        first_name text,
        last_name text,
        secque text
    )""")

# null, integer, real, text, blob

def startDB():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()



def deleteTable():
    c.execute("DROP TABLE userdata")

def insertRow(username, password, first_name, last_name, secque):
    try:
        c.execute(f"INSERT INTO userdata VALUES ('{username}','{password}','{first_name}','{last_name}','{secque}')")
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
#
# username = "wasd"
# password = "wasd"
# first_name = "wasd"
# last_name = "wasd"
# secque = [["5","wasd"],["2","wasd"]]
#
# insertRow(username, password, first_name, last_name, list_to_string(secque))
#
# finDB()