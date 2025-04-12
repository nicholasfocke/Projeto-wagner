from validacoes import nome_valido, senha_valida

def cadastrar(usuarios):
    print('--Área de cadastro--')
    nome = input("Digite o nome do usuário: ").strip().lower()

    if nome in usuarios:
        print("⚠️ Usuário já cadastrado.")
        return

    if not nome_valido(nome):
        print("⚠️ Nome de usuário inválido! Use apenas letras e números.")
        return

    senha = input('Digite a senha: ').strip()
    if not senha_valida(senha):
        print("⚠️ Senha inválida! Use apenas letras ou números e mínimo 3 caracteres.")
        return

    usuarios[nome] = senha
    print("✅ Usuário cadastrado com sucesso!")
