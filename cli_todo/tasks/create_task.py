import sqlite3

conexao = sqlite3.connect('../todo.sqlite3')
cursor = conexao.cursor()

print("Escreva os dados da Tarefa: ")
nome = input("Nome: ")
data = input("Data ")
status = input("Status: ")

print("Categorias disponíveis: ")
categorias_disponiveis = "select * from categoria"
consulta = cursor.execute(categorias_disponiveis)
for resultado in consulta:
    print(resultado)

# cursor.execute(categorias_disponiveis)

categoria_id = input("Selecione o ID da categoria que essa tarefa pertence: ")

print("Tarefa inserida com sucesso!")

valores = [nome, data, status, categoria_id]
sql_inserir = 'insert into tarefa (nome, data, status, categoria_id) values (?, ?, ?, ?)'
cursor = conexao.cursor()
cursor.execute(sql_inserir, valores)
conexao.commit()
conexao.close()
