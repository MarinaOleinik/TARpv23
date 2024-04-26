from sqlite3 import *
from sqlite3 import Error
from os import *

def create_connect(path:str):
    connection=None
    try:
        connection=connect(path)
        print("Ühendus on olemas!")
    except Error as e:
        print(f"Tekkis viga: {e}")
    return connection
def execute_query(connection,query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud")
    except Error as e:
        print(f"Tekkis viga: {e}")
def execute_read_query(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"Tekkis viga: {e}")

create_users_table="""
CREATE TABLE IF NOT EXISTS users(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Lname TEXT NOT NULL,
Age INTEGER NOT NULL,
Gender TEXT
)
"""
insert_users="""
INSERT INTO
users(Name,Lname,Age,Gender)
VALUES
('Mati','Tamm',50,'mees'),
('Kati','Kask',54,'mees'),
('Margus','Tamm',12,'mees'),
('Anna','Kuusk',44,'mees')
"""
select_users="SELECT * from users"

filename=path.abspath(__file__)
dbdir=filename.rstrip('Too_andmebaasiga.py')
dbpath=path.join(dbdir,"data.db")
conn=create_connect(dbpath)
execute_query(conn,create_users_table)
execute_query(conn,insert_users)
users=execute_read_query(conn,select_users)
print("Kautajate tabel:")
for user in users:
    print(user)