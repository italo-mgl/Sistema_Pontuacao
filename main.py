import sqlite3 as lite
from sqlite3 import Error

conexao = lite.connect("tutorial.db")

with conexao:
    cursor = conexao.cursor()
    cursor.execute("""CREATE TABLE login(id
                        INTEGER PRIMARY KEY AUTOINCREMENT,
                   Usuario VARCHAR,
                   SENHA VARCHAR)
                   """)
