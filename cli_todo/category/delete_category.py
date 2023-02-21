import sqlite3

conexao = sqlite3.connect('../todo.sqlite3')
cursor = conexao.cursor()

print("Categorias disponíveis: ")
categorias_disponiveis = "select * from categoria"
consulta = cursor.execute(categorias_disponiveis)
for resultado in consulta:
    print(resultado)

deletar_categoria = input("Digite o ID da categoria que deseja excluir: ")
print(f'{resultado} removido com sucesso.')
valores = [deletar_categoria]
sql = 'delete from categoria where id = ?'
cursor.execute(sql, valores)
conexao.commit()
conexao.close()
