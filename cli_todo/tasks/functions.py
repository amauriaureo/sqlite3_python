import sqlite3
# import '../category/functions' as fun


def mostrar_categoria():
    conexao = sqlite3.connect('../todo.sqlite3')
    cursor = conexao.cursor()
    print("Categorias disponíveis: ")
    consulta = cursor.execute("select * from categoria")
    for resultado in consulta:
        print(f'ID: {resultado[0]} || Categoria: {resultado[1]}')


def mostrar_tarefas():
    conexao = sqlite3.connect('../todo.sqlite3')
    cursor = conexao.cursor()
    print("Tarefas disponíveis: ")
    consulta = cursor.execute("select * from tarefa")
    for resultado in consulta:
        print(f'ID: {resultado[0]} || Tarefa: {resultado[1]}')


def criar_tarefa():
    conexao = sqlite3.connect('../todo.sqlite3')
    cursor = conexao.cursor()

    print("Escreva os dados da Tarefa: ")
    nome = input("Nome: ")
    data = input("Data ")
    status = input("Status: ")

    mostrar_categoria()

    categoria_id = input("Selecione o ID da categoria que essa tarefa pertence: ")

    print("Tarefa inserida com sucesso!")

    valores = [nome, data, status, categoria_id]
    sql_inserir = 'insert into tarefa (nome, data, status, categoria_id) values (?, ?, ?, ?)'
    cursor = conexao.cursor()
    cursor.execute(sql_inserir, valores)
    conexao.commit()
    conexao.close()


def deletar_tarefa():
    conexao = sqlite3.connect('../todo.sqlite3')
    cursor = conexao.cursor()

    print("Tarefas disponíveis: ")
    tarefas_disponiveis = "select * from tarefa"
    consulta = cursor.execute(tarefas_disponiveis)
    for resultado in consulta:
        print(resultado)

    deletar_tarefa = input("Digite o ID da tarefa que deseja excluir: ")
    print(f'{resultado[1]} removido com sucesso.')
    valores = [deletar_tarefa]
    sql = 'delete from tarefa where id = ?'
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()


def atualizar_tarefa():
    conexao = sqlite3.connect('../todo.sqlite3')
    cursor = conexao.cursor()
    mostrar_tarefas()
    atualizar = input("Digite o ID da tarefa que deseja atualizar: ")
    nome = input("Digite o nome da tarefa: ")
    data = input("Digite a data da tarefa: ")
    status = input("Digite o Status da tarefa: ")
    mostrar_categoria()
    categoria_id = input("Digite o ID da categoria da tarefa: ")

    sql = 'update tarefa set nome = ?, data = ?, status = ?, categoria_id = ? where id = ? '

    valores = [nome, data, status, categoria_id, atualizar]
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()


atualizar_tarefa()
