def excluir(usuarios, usuario_logado):
    print("\n-- Excluir Usuário --")

    if usuario_logado == "admin":
        nome = input("Digite o nome do usuário que deseja excluir: ").strip().lower()
        usuario_alvo = None
        for usuario in usuarios:
            if usuario['nome'] == nome:
                usuario_alvo = usuario
                break
        if not usuario_alvo:
            print("❌ Usuário não encontrado.")
            return usuario_logado
        if nome == "admin":
            print("⚠️ O administrador não pode excluir sua própria conta.")
            return usuario_logado
    else:
        nome = usuario_logado
        usuario_alvo = None
        for usuario in usuarios:
            if usuario['nome'] == nome:
                usuario_alvo = usuario
                break

    confirmacao = input(f"Tem certeza que deseja excluir '{nome}'? (s/n): ").lower()
    if confirmacao == "s" or confirmacao == "sim":
        usuarios.remove(usuario_alvo)
        print(f"✅ Usuário '{nome}' excluído com sucesso.")
        if nome == usuario_logado:
            return None

    return usuario_logado

def excluir_registro_extravio(registros_extravio, usuario_logado):
    if not registros_extravio:
        print("\nNenhum registro de extravio cadastrado.")
        return usuario_logado
    print("\n--- Registros de Extravio ---")
    for i, registro in enumerate(registros_extravio, 1):
        print(f"{i} - Passageiro: {registro['Passageiro']['nome']} | Voo: {registro['Voo']['numero_voo']}")
    try:
        while True:
            escolha = input("Digite o número do registro que deseja excluir (0 para voltar): ").strip()
            if escolha and escolha.isdigit():
                escolha = int(escolha)
                break
            print("Digite um número válido.")
        if escolha == 0:
            return usuario_logado
        if 1 <= escolha <= len(registros_extravio):
            while True:
                confirmacao = input(f"Tem certeza que deseja excluir o registro {escolha}? (s/n): ").strip().lower()
                if confirmacao and confirmacao.isalpha():
                    break
                print("Confirmação deve ser uma resposta de sim ou não (s/n).")
            if confirmacao == "s" or confirmacao == "sim":
                excluido = registros_extravio.pop(escolha - 1)
                print(f"✅ Registro do passageiro '{excluido['Passageiro']['nome']}' excluído com sucesso.")
            else:
                print("Operação cancelada.")
        else:
            print("Opção inválida.")
    except (ValueError, IndexError):
        print("Opção inválida.")

    return usuario_logado