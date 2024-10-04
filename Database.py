import sqlite3
import json

conn = sqlite3.connect('database.db')
c = conn.cursor()

# null, integer, real, text, blob

def startDB():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

def createTable():
    c.execute("""CREATE TABLE userdata (
            username text,
            password text,
            first_name text,
            last_name text,
            secque text
        )""")

def deleteTable():
    c.execute("DROP TABLE userdata")

def insertRow(username, password, first_name, last_name, secque):
    c.execute(f"INSERT INTO userdata VALUES ('{username}','{password}','{first_name}','{last_name}','{secque}')")

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

# username = "wasd"
# password = "wasd"
# first_name = "wasd"
# last_name = "wasd"
# secque = [["5","wasd"],["2","wasd"]]
#
# insertRow(username, password, first_name, last_name, list_to_string(secque))
#
# finDB()