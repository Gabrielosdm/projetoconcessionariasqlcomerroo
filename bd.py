# Função validar login
def get_idfuncionarios(cursor, login, senha):
    # Executar o sql
    cursor.execute(f'select idfuncionarios from login where login = "{login}" and senha = "{senha}"')

    # Recuperando o retorno do BD
    idfuncionarios = cursor.fetchone()

    # Fechar o cursor
    cursor.close()

    # Retornar o idfuncionarios
    return idfuncionarios[0]