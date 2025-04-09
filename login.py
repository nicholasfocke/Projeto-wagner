# login.py
from validacoes import senha_valida

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
