import sqlite3
conexao = sqlite3.connect('todo.sqlite3')

cursor = conexao.cursor()


sql = '''
create table tarefa (
    nome VARCHAR(20),
    data VARCHAR(20),
    status VARCHAR(20),
    categoria_id INT NOT NULL,
        FOREIGN KEY (categoria_id) REFERENCES categoria(id)
)

'''

cursor.execute(sql)
conexao.commit()
conexao.close()
