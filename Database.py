import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# null, integer, real, text, blob

def createTable():
    c.execute("""CREATE TABLE userdata (
            username text,
            password text,
            first_name text,
            last_name text
        )""")

def deleteTable():
    c.execute("DROP TABLE userdata")

def insertRow(username, password, first_name, last_name):
    c.execute(f"INSERT INTO userdata VALUES ('{username}','{password}','{first_name}','{last_name}')")

def getData():
    c.execute("SELECT * FROM userdata")
    return c.fetchall()


#createTable()
#deleteTable()
#insertRow("wilki","1234","ben","wilkinson")

conn.commit()

conn.close()
