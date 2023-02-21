import sqlite3

conexao = sqlite3.connect('../todo.sqlite3')
cursor = conexao.cursor()

print("Categorias disponíveis: ")
categorias_disponiveis = "select * from categoria"
consulta = cursor.execute(categorias_disponiveis)
for resultado in consulta:
    print(resultado)

categoria_id = input("Digite o ID da categoria que deseja atualizar? ")

nome = input("Informe o novo nome da categoria: ")
print("Categoria atualizada com sucesso!")

sql = 'update categoria set nome = ? where id = ?'
valores = [nome, categoria_id]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()
