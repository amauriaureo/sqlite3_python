import sqlite3
conexao = sqlite3.connect('todo.sqlite3')

cursor = conexao.cursor()


sql = '''
create table tarefa (
    id INTEGER PRIMARY KEY NOT NULL,
    nome VARCHAR(20),
    data VARCHAR(20),
    status VARCHAR(20),
    categoria_id INT NOT NULL,
        FOREIGN KEY (categoria_id) REFERENCES categoria(id)
)

'''
# id = 10
# nome = 'Iago'
# data = '01/03/2023'
# status = 'em andamento'
# categoria_id = 2
# sql2 = ('''
# INSERT INTO tarefa3 (id, nome, data, status, categoria_id)
# VALUES (?, ?, ?, ?, ?)
# ''', (id, nome, data, status, categoria_id))

cursor.execute(sql)
conexao.commit()
conexao.close()
