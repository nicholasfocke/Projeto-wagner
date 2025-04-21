def excluir(usuarios, usuario_logado):
    print("\n-- Excluir Usuário --")

    if usuario_logado == "admin":
        nome = input("Digite o nome do usuário que deseja excluir: ").strip().lower()
        if nome not in usuarios:
            print("❌ Usuário não encontrado.")
            return usuario_logado
        if nome == "admin":
            print("⚠️ O administrador não pode excluir sua própria conta.")
            return usuario_logado
    else:
        nome = usuario_logado

    confirmacao = input(f"Tem certeza que deseja excluir '{nome}'? (s/n): ").lower()
    if confirmacao == "s":
        del usuarios[nome]
        print(f"✅ Usuário '{nome}' excluído com sucesso.")
        if nome == usuario_logado:
            return None
    return usuario_logado