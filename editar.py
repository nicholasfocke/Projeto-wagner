from validacoes import senha_valida, nome_valido

def editar(usuarios, usuario_logado):
    print(f"\n-- Edição de dados do usuário: {usuario_logado} --")

    usuario_alvo = None
    if usuario_logado == "admin":
        alvo = input("Digite o nome do usuário que deseja editar: ").strip().lower()
        for usuario in usuarios:
            if usuario['nome'] == alvo:
                usuario_alvo = usuario
                break
            
        if not usuario_alvo:
            print("❌ Usuário não encontrado.")
            return usuario_logado
    else:
        for usuario in usuarios:
            if usuario['nome'] == usuario_logado:
                usuario_alvo = usuario
                break

    novo_nome = input("Novo nome de usuário (pressione Enter para manter o mesmo): ").strip().lower()
    nova_senha = input("Nova senha (pressione Enter para manter a mesma): ").strip()

    if not novo_nome and not nova_senha:
        print("⚠️ Nenhuma alteração feita.")
        return usuario_logado

    if usuario_logado == "admin" and usuario_alvo['nome'] == "admin" and novo_nome:
        print("⚠️ O administrador não pode alterar seu próprio nome de usuário.")
        return usuario_logado

    if novo_nome:
        if not nome_valido(novo_nome):
            print("⚠️ Nome inválido! Use apenas letras e números.")
            return usuario_logado
        
        for usuario in usuarios:
            if usuario['nome'] == novo_nome:
                print("⚠️ Nome já existente.")
                return usuario_logado

    if nova_senha:
        if not senha_valida(nova_senha):
            print("⚠️ Senha inválida! Deve conter apenas letras ou números e ter no mínimo 3 caracteres.")
            return usuario_logado

    if novo_nome:
        usuario_alvo['nome'] = novo_nome
        print(f"✅ Nome alterado para '{novo_nome}'.")

    if nova_senha:
        usuario_alvo['senha'] = nova_senha
        print("✅ Senha atualizada com sucesso.")

    # Retornar o nome atualizado ou o atual
    return novo_nome if novo_nome else usuario_logado