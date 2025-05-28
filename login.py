from validacoes import senha_valida
import hashlib

def login(cursor):
    print('--Login--')
    nome = input("Digite o nome do usuário: ").strip().lower()

    cursor.execute("SELECT senha FROM usuarios WHERE nome = %s", (nome,))
    resultado = cursor.fetchone()
    if resultado:
        senha = input("Digite sua senha: ").strip()
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        cursor.execute("SELECT * FROM usuarios WHERE nome = %s AND senha = %s", (nome, senha_hash))
        if cursor.fetchone():
            print("✅ Login realizado com sucesso!")
            return nome
        else:
            print("❌ Usuário ou senha incorretos.")
            return None

    print("❌ Usuário não encontrado!")
    return None