import sqlite3


def mostrar_categoria():
    conexao = sqlite3.connect('../todo.sqlite3')
    cursor = conexao.cursor()
    print("Categorias disponíveis: ")
    consulta = cursor.execute("select * from categoria")
    for resultado in consulta:
        print(f'ID: {resultado[0]} || Categoria: {resultado[1]}')


def criar_categoria():
    mostrar_categoria()
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


def deletar_categoria():
    mostrar_categoria()
    conexao = sqlite3.connect('../todo.sqlite3')
    cursor = conexao.cursor()
    deletar_categoria = input("Digite o ID da categoria que deseja excluir: ")
    print('Removido com sucesso.')
    valores = [deletar_categoria]
    sql = 'delete from categoria where id = ?'
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()


def atualizar_categoria():
    mostrar_categoria()
    conexao = sqlite3.connect('../todo.sqlite3')
    cursor = conexao.cursor()

    categoria_id = input("Digite o ID da categoria que deseja atualizar? ")

    nome = input("Informe o novo nome da categoria: ")
    print("Categoria atualizada com sucesso!")

    sql = 'update categoria set nome = ? where id = ?'
    valores = [nome, categoria_id]
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close()


# def mostrar_categoria2():
#     conexao = sqlite3.connect('../todo.sqlite3')
#     cursor = conexao.cursor()
#     print("Categorias disponíveis: ")
#     cursor.execute("select * from categoria")
#     consulta = cursor.fetchall()
#     for resultado in consulta:
#         print(f'ID: {resultado[0]} || Categoria: {resultado[1]}')


# mostrar_categoria2()
