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
    if confirmacao == "s":
        usuarios.remove(usuario_alvo)
        print(f"✅ Usuário '{nome}' excluído com sucesso.")
        if nome == usuario_logado:
            return None

    return usuario_logado