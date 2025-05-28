from validacoes import nome_valido, senha_valida
import hashlib

def cadastrar(cursor, conn):
    print('--Área de cadastro--')
    nome = input("Digite o nome do usuário: ").strip().lower()

    cursor.execute("SELECT nome FROM usuarios WHERE nome = %s", (nome,))
    if cursor.fetchone():
        print("⚠️ Usuário já cadastrado.")
        return

    if not nome_valido(nome):
        print("⚠️ Nome de usuário inválido! Use apenas letras e números.")
        return

    senha = input('Digite a senha: ').strip()
    if not senha_valida(senha):
        print("⚠️ Senha inválida! Use apenas letras ou números e mínimo 3 caracteres.")
        return

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (%s, %s)", (nome, senha_hash))
    conn.commit()
    print("✅ Usuário cadastrado com sucesso!")