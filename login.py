from validacoes import senha_valida

def login(cursor):
    print('--Login--')
    nome = input("Digite o nome do usuário: ").strip().lower()

    cursor.execute("SELECT senha FROM usuarios WHERE nome = %s", (nome,))
    resultado = cursor.fetchone()
    if resultado:
        senha = input("Digite a senha: ").strip()
        if senha_valida(senha) and resultado[0] == senha:
            print("✅ Entrou no sistema.")
            return nome
        else:
            print("❌ Senha incorreta ou inválida.")
            return None

    print("❌ Usuário não encontrado!")
    return None