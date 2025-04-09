
def exibir(usuarios):
    print('\n--Lista de usuários--')
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
    else:
        for nome in usuarios:
            print(f'- {nome}')