def exibir(usuarios):
    print('\n--Lista de usuários--')
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"- Nome: {usuario['nome']}")