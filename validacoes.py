def nome_valido(nome):
    return nome.isalnum()

def senha_valida(senha):
    return senha.isalnum() and len(senha) >= 3