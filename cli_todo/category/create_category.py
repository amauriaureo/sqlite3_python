import sqlite3

conexao = sqlite3.connect('../todo.sqlite3')

print("Vamos criar uma categora?")
nome = input("Insira o nome da categoria: ")
print("Categoria inserida com sucesso!")

valores = [nome]
sql_inserir_categoria = 'insert into categoria (nome) values (?)'
cursor = conexao.cursor()
cursor.execute(sql_inserir_categoria, valores)
conexao.commit()
conexao.close()
