import sqlite3

conexao = sqlite3.connect('../todo.sqlite3')
cursor = conexao.cursor()

print("Categorias disponíveis: ")
categorias_disponiveis = "select * from categoria"
consulta = cursor.execute(categorias_disponiveis)
for resultado in consulta:
    print(resultado)

cursor.execute(categorias_disponiveis)
conexao.commit()
conexao.close()
