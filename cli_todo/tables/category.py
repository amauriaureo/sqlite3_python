import sqlite3
conexao = sqlite3.connect('todo.sqlite3')

cursor = conexao.cursor()

sql = '''
create table categoria (
    id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(20)
)

'''


cursor.execute(sql)
conexao.commit()
conexao.close()
