from validacoes import senha_valida, nome_valido

def editar(usuarios, usuario_logado):
    print(f"\n-- Edição de dados do usuário: {usuario_logado} --")

    if usuario_logado == "admin":
        alvo = input("Digite o nome do usuário que deseja editar: ").strip().lower()
        if alvo not in usuarios:
            print("❌ Usuário não encontrado.")
            return usuario_logado
    else:
        alvo = usuario_logado

    novo_nome = input("Novo nome de usuário (pressione Enter para manter o mesmo): ").strip().lower()
    nova_senha = input("Nova senha (pressione Enter para manter a mesma): ").strip()

    if novo_nome == "" and nova_senha == "":
        print("⚠️ Nenhuma alteração feita.")
        return usuario_logado

    if novo_nome and (not nome_valido(novo_nome) or novo_nome in usuarios):
        print("⚠️ Nome inválido ou já existente.")
        return usuario_logado

    if nova_senha and not senha_valida(nova_senha):
        print("⚠️ Senha inválida! Deve conter apenas letras ou números e 3 caracteres.")
        return usuario_logado

    novo_nome_final = novo_nome if novo_nome else alvo
    nova_senha_final = nova_senha if nova_senha else usuarios[alvo]

    usuarios[novo_nome_final] = nova_senha_final

    if novo_nome and novo_nome != alvo:
        del usuarios[alvo]
        print(f"✅ Nome alterado para '{novo_nome_final}'.")

    if nova_senha:
        print("✅ Senha atualizada com sucesso.")

    if alvo == usuario_logado:
        return novo_nome_final
    else:
        return usuario_logado