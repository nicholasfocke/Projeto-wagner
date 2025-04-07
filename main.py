import os

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

def nome_valido(nome):
    return nome.isalnum()

def senha_valida(senha):
    return senha.isalnum() and senha != ""

def login(usuarios):
    print('--Login--')
    nome = input("Digite o nome do usuário: ").strip().lower()
    if nome not in usuarios:
        print("❌ Usuário não encontrado!")
        return None
    senha = input("Digite a senha: ").strip()
    if senha_valida(senha) and usuarios[nome] == senha:
        print("✅ Entrou no sistema.")
        return nome
    else:
        print("❌ Senha incorreta ou inválida.")
        return None

def editar(usuarios, usuario_logado):
    print(f"\n-- Edição de dados do usuário: {usuario_logado} --")

    if usuario_logado == "admin":
        alvo = input("Digite o nome do usuário que deseja editar: ").strip().lower()
        if alvo not in usuarios:
            print("❌ Usuário não encontrado.")
            return usuario_logado
    else:
        alvo = usuario_logado

    novo_nome = input("Novo nome de usuário (pressione Enter para manter o mesmo): ").strip().lower()
    nova_senha = input("Nova senha (pressione Enter para manter a mesma): ").strip()

    if novo_nome == "" and nova_senha == "":
        print("⚠️ Nenhuma alteração feita.")
        return usuario_logado

    if novo_nome and (not nome_valido(novo_nome) or novo_nome in usuarios):
        print("⚠️ Nome inválido ou já existente.")
        return usuario_logado

    if nova_senha and not senha_valida(nova_senha):
        print("⚠️ Senha inválida! Deve conter apenas letras ou números.")
        return usuario_logado

    novo_nome_final = novo_nome if novo_nome else alvo
    nova_senha_final = nova_senha if nova_senha else usuarios[alvo]

    usuarios[novo_nome_final] = nova_senha_final

    if novo_nome and novo_nome != alvo:
        del usuarios[alvo]
        print(f"✅ Nome alterado para '{novo_nome_final}'.")

    if nova_senha:
        print("✅ Senha atualizada com sucesso.")

    if alvo == usuario_logado:
        return novo_nome_final
    else:
        return usuario_logado

def excluir(usuarios, usuario_logado):
    print("\n-- Excluir Usuário --")

    if usuario_logado == "admin":
        nome = input("Digite o nome do usuário que deseja excluir: ").strip().lower()
        if nome not in usuarios:
            print("❌ Usuário não encontrado.")
            return usuario_logado
    else:
        nome = usuario_logado

    confirmacao = input(f"Tem certeza que deseja excluir '{nome}'? (s/n): ").lower()
    if confirmacao == "s":
        del usuarios[nome]
        print(f"✅ Usuário '{nome}' excluído com sucesso.")
        if nome == usuario_logado:
            return None
    return usuario_logado

def cadastrar(usuarios):
    print('--Área de cadastro--')
    nome = input("Digite o nome do usuário: ").strip().lower()

    if nome in usuarios:
        print("⚠️ Usuário já cadastrado.")
        return
    if not nome_valido(nome):
        print("⚠️ Nome de usuário inválido! Use apenas letras.")
        return

    senha = input('Digite a senha: ').strip()
    if not senha_valida(senha):
        print("⚠️ Senha inválida! Use apenas letras ou números.")
        return

    usuarios[nome] = senha
    print("✅ Usuário cadastrado com sucesso!")

def exibir(usuarios):
    print('\n--Lista de usuários--')
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
    else:
        for nome in usuarios:
            print(f'- {nome}')

def main():
    usuarios = {"admin": "admin123"}
    usuario_logado = None

    while True:
        if usuario_logado:
            menu_logado(usuario_logado)
            opcao = input("Escolha uma opção: ").strip()
            os.system('cls')

            if opcao == "1":
                exibir(usuarios)

            elif opcao == "2":
                usuario_logado = editar(usuarios, usuario_logado)

            elif opcao == "3":
                usuario_logado = excluir(usuarios, usuario_logado)

            elif opcao == "0":
                print("👋 Logout realizado com sucesso!")
                usuario_logado = None

            else:
                print("⚠️ Opção inválida! Tente novamente.")
            
        else:
            menu_geral()
            opcao = input("Escolha uma opção: ").strip()
            os.system('cls')

            if opcao == "1":
                usuario_logado = login(usuarios)

            elif opcao == "2":
                cadastrar(usuarios)

            elif opcao == "3":
                print("👋 Programa encerrado. Até logo!")
                break

            else:
                print("⚠️ Opção inválida! Tente novamente.")

main()