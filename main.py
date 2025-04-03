def menu_geral():
    print('--Bem vindo ao sistema de extravio de bagagem--')
    print('--Clique na opção que deseja abaixo--')
    print("1 - Login")
    print("2 - Cadastrar Usuário")
    print("3 - Sair")

def menu_logado(usuario):
    print(f"\n-- MENU DO USUÁRIO: {usuario} --")
    print("1 - Editar Usuário")
    print("2 - Exibir Usuários")
    print("3 - Excluir Usuário")
    print("0 - Sair")

def senha_valida(senha):
    if senha != "" and not senha.isspace():
        return True
    else:
        return False

def login(usuarios):
    print('--Login--')
    nome = input("Digite o nome do usuário: ").strip()
    if nome not in usuarios:
        print("❌ Usuário não encontrado!")
        return None
    try:
        senha = input("Digite a senha: ")
        if senha_valida(senha) and usuarios[nome] == senha:
            print("✅ Entrou no sistema.")
            return nome
        else:
            print("❌ Senha incorreta ou inválida.")
            return None
    except Exception as e:
        print("⚠️ Erro ao tentar logar.", e)
        return None

def cadastrar(usuarios):
    print('--Área de cadastro--')
    nome = input("Digite o nome do usuário: ").strip()
    if nome in usuarios:
        print("⚠️ Usuário já cadastrado.")
        return
    try:
        senha = input('Digite a senha: ')
        if senha_valida(senha):
            usuarios[nome] = senha
            print("✅ Usuário cadastrado com sucesso!")
        else:
            print("⚠️ Senha inválida! Não pode ser vazia ou apenas espaços.")
    except Exception as e:
        print("⚠️ Erro ao cadastrar o usuário:", e)



def main():
    usuarios = {}
    usuario_logado = None

    while True:
        if usuario_logado:
            menu_logado(usuario_logado)
            opcao = input("Escolha uma opção: ").strip()

        else:
            menu_geral()
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                usuario_logado = login(usuarios)
            elif opcao == "2":
                cadastrar(usuarios)
            elif opcao == "3":
                print("👋 Saindo do sistema. Até logo!")
                break
            else:
                print("⚠️ Opção inválida! Tente novamente.")

main()