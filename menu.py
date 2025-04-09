def menu_geral():
    print('\n--Bem vindo ao sistema de extravio de bagagem--')
    print('--Clique na opção que deseja abaixo--')
    print("1 - Login")
    print("2 - Cadastrar Usuário")
    print("3 - Sair")

def menu_logado(usuario):
    print(f"\n-- MENU DO USUÁRIO: {usuario} --")
    print("1 - Exibir Usuários")
    print("2 - Editar Usuário")
    print("3 - Excluir Usuário")
    print("0 - Sair")