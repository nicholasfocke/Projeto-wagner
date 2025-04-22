from validacoes import senha_valida

def login(usuarios):
    print('--Login--')
    nome = input("Digite o nome do usuário: ").strip().lower()

    for usuario in usuarios:
        if usuario['nome'] == nome:
            senha = input("Digite a senha: ").strip()
            if senha_valida(senha) and usuario['senha'] == senha:
                print("✅ Entrou no sistema.")
                return nome
            else:
                print("❌ Senha incorreta ou inválida.")
                return None

    print("❌ Usuário não encontrado!")
    return None