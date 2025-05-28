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

    return novo_nome if novo_nome else usuario_logado

def editar_registro_extravio(registros_extravio, usuario_logado):
    if not registros_extravio:
        print("\nNenhum registro de extravio cadastrado.")
        return usuario_logado
    print("\n--- Registros de Extravio ---")
    for i, registro in enumerate(registros_extravio, 1):
        print(f"{i} - Passageiro: {registro['Passageiro']['nome']} | Voo: {registro['Voo']['numero_voo']}")
    try:
        escolha = int(input("Digite o número do registro que deseja editar (0 para voltar): ").strip())
        if escolha == 0:
            return usuario_logado
        if 1 <= escolha <= len(registros_extravio):
            registro = registros_extravio[escolha - 1]
            print("\n--- Editando Registro ---")
            for chave, valor in registro.items():
                print(f"{chave}: {valor}")
            print("Deixe em branco para manter o valor atual ⚠️.")

            novo_nome = input(f"Novo nome do passageiro [{registro['Passageiro']['nome']}]: ").strip()
            if novo_nome:
                if novo_nome and all(parte.isalpha() for parte in novo_nome.split()):
                    registro['Passageiro']['nome'] = novo_nome
                else:
                    print("⚠️ Digite apenas letras e espaços no nome, sem números ou sinais.")
            novo_email = input(f"Novo e-mail [{registro['Passageiro']['email']}]: ").strip()
            if novo_email:
                if "@" in novo_email and ".com" in novo_email and novo_email.isalnum() == False:
                    registro['Passageiro']['email'] = novo_email
                else:
                    print("⚠️ E-mail deve conter '@' e '.com'.")
            novo_documento = input(f"Novo documento [{registro['Passageiro']['documento']}]: ").strip()
            if novo_documento:
                if novo_documento.isdigit() and len(novo_documento) >= 8:
                    registro['Passageiro']['documento'] = novo_documento
                else:
                    print("⚠️ Documento deve conter apenas números e ter pelo menos 8 dígitos.")
            novo_data_nasc = input(f"Nova data de nascimento [{registro['Passageiro']['data_nascimento']}]: ").strip()
            if novo_data_nasc:
                if (
                    novo_data_nasc
                    and all(c.isdigit() or c == '-' for c in novo_data_nasc)
                    and len(novo_data_nasc.replace("-", "")) >= 8
                ):
                    registro['Passageiro']['data_nascimento'] = novo_data_nasc
                else:
                    print("⚠️ Data de nascimento não pode estar vazia, só pode conter números e traços, e deve ter pelo menos 8 dígitos.")

            novo_numero_voo = input(f"Novo ticket do voo [{registro['Voo']['numero_voo']}]: ").strip()
            if novo_numero_voo:
                if novo_numero_voo.isalnum():
                    registro['Voo']['numero_voo'] = novo_numero_voo
                else:
                    print("⚠️ Número do voo deve ser números e letras ou apenas números.")
            nova_origem = input(f"Nova origem [{registro['Voo']['origem']}]: ").strip()
            if nova_origem:
                if nova_origem.isalpha():
                    registro['Voo']['origem'] = nova_origem
                else:
                    print("⚠️ Origem deve conter apenas letras.")
            novo_destino = input(f"Novo destino [{registro['Voo']['destino']}]: ").strip()
            if novo_destino:
                if novo_destino.isalpha():
                    registro['Voo']['destino'] = novo_destino
                else:
                    print("⚠️ Destino deve conter apenas letras.")
            novo_horario = input(f"Novo horário [{registro['Voo']['horario']}]: ").strip()
            if novo_horario:
                if novo_horario and all(c.isdigit() or c == ':' for c in novo_horario):
                    registro['Voo']['horario'] = novo_horario
                else:
                    print("⚠️ Horário não pode estar vazio e só pode conter números e dois pontos.")

            novo_assento = input(f"Novo assento [{registro['Passageiro no Voo']['assento']}]: ").strip()
            if novo_assento:
                if novo_assento and novo_assento.isalnum():
                    registro['Passageiro no Voo']['assento'] = novo_assento
                else:
                    print("⚠️ Assento não pode estar vazio e deve conter letras e números.")
            nova_classe = input(f"Nova classe [{registro['Passageiro no Voo']['classe']}]: ").strip()
            if nova_classe:
                if nova_classe and nova_classe.isalpha():
                    registro['Passageiro no Voo']['classe'] = nova_classe
                else:
                    print("⚠️ Classe não pode estar vazia e deve conter apenas letras.")

            nova_cor = input(f"Nova cor [{registro['Bagagem']['cor']}]: ").strip()
            if nova_cor:
                if nova_cor.isalpha():
                    registro['Bagagem']['cor'] = nova_cor
                else:
                    print("⚠️ Digite apenas letras para a cor.")
            nova_marca = input(f"Nova marca [{registro['Bagagem']['marca']}]: ").strip()
            if nova_marca:
                if nova_marca.isalpha():
                    registro['Bagagem']['marca'] = nova_marca
                else:
                    print("⚠️ Digite apenas letras para a marca.")
            novo_peso = input(f"Novo peso [{registro['Bagagem']['peso']}]: ").strip()
            if novo_peso:
                try:
                    registro['Bagagem']['peso'] = float(novo_peso)
                except ValueError:
                    print("⚠️ Peso deve ser um número (pode ser decimal).")

            nova_data_hora = input(f"Nova data e hora do extravio [{registro['Ocorrência']['data_hora']}]: ").strip()
            if nova_data_hora:
                if nova_data_hora and all(c.isdigit() or c in "- :" for c in nova_data_hora):
                    registro['Ocorrência']['data_hora'] = nova_data_hora
                else:
                    print("⚠️ Data e hora não pode estar vazia e só pode conter números, traços, espaço e dois pontos.")

            nova_descricao = input(f"Nova descrição de danificação [{registro['Danificação']['descricao']}]: ").strip()
            if nova_descricao:
                registro['Danificação']['descricao'] = nova_descricao

            novo_endereco = input(f"Novo endereço de entrega [{registro['Entrega']['endereco_entrega']}]: ").strip()
            if novo_endereco:
                registro['Entrega']['endereco_entrega'] = novo_endereco

            print("✅ Registro de extravio atualizado com sucesso.")
        else:
            print("Opção inválida.")
    except (ValueError, IndexError):
        print("Opção inválida.")
    return usuario_logado