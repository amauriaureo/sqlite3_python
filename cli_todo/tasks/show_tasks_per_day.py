import sqlite3

conexao = sqlite3.connect('../todo.sqlite3')
cursor = conexao.cursor()

print("Vamos filtrar as tarefas pela data.")
print("Essas são as datas que estão com alguma tarefa incluída: ")
datas_disponiveis = '''
select data from tarefa
'''
consulta = cursor.execute(datas_disponiveis)
for resultado in consulta:
    print(resultado)

tarefas_por_dia = input("Digite a data desejada: ")
valores = [tarefas_por_dia]

consultadois = '''
select from tarefa where data = ?
'''

cursor.execute(valores)
conexao.commit()
conexao.close()
