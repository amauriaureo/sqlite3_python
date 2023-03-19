# import functions as fun

# fun.deletar_tarefa()
import sqlite3


def deletar_tarefa():
    conexao = sqlite3.connect('../todo.sqlite3')
    cursor = conexao.cursor()

    print("Tarefas disponíveis: ")
    tarefas_disponiveis = "select * from tarefa"
    consulta = cursor.execute(tarefas_disponiveis)
    for resultado in consulta:
        print(resultado)

    deletar_tarefa = input("Digite o ID da tarefa que deseja excluir(0 para sair): ")
    if deletar_tarefa == "0":
        print("Saindo do serviço de deletar tarefa")
    else:
        print(f'{resultado[1]} removido com sucesso.')
    valores = [deletar_tarefa]

    sql = 'delete from tarefa where id = ?'
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()


deletar_tarefa()
