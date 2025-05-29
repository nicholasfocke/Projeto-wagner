from validacoes import senha_valida, nome_valido

def editar(cursor, conn, usuario_logado):
    print(f"\n-- Edição de dados do usuário: {usuario_logado} --")

    if usuario_logado == "admin":
        alvo = input("Digite o nome do usuário que deseja editar: ").strip().lower()
        cursor.execute("SELECT nome FROM usuarios WHERE LOWER(nome) = %s", (alvo,))
        usuario_alvo = cursor.fetchone()
        if not usuario_alvo:
            print("❌ Usuário não encontrado.")
            return usuario_logado
        if alvo == "admin":
            print("⚠️ O administrador não pode alterar seu próprio nome de usuário.")
            return usuario_logado
        nome_usuario = alvo
    else:
        cursor.execute("SELECT nome FROM usuarios WHERE nome = %s", (usuario_logado,))
        usuario_alvo = cursor.fetchone()
        nome_usuario = usuario_logado

    novo_nome = input("Novo nome de usuário (pressione Enter para manter o mesmo): ").strip().lower()
    nova_senha = input("Nova senha (pressione Enter para manter a mesma): ").strip()

    if not novo_nome and not nova_senha:
        print("⚠️ Nenhuma alteração feita.")
        return usuario_logado

    if novo_nome:
        if not nome_valido(novo_nome):
            print("⚠️ Nome inválido! Use apenas letras e números.")
            return usuario_logado
        cursor.execute("SELECT nome FROM usuarios WHERE nome = %s", (novo_nome,))
        if cursor.fetchone():
            print("⚠️ Nome já existente.")
            return usuario_logado

    if nova_senha:
        if not senha_valida(nova_senha):
            print("⚠️ Senha inválida! Deve conter apenas letras ou números e ter no mínimo 3 caracteres.")
            return usuario_logado

    if novo_nome:
        cursor.execute("UPDATE usuarios SET nome = %s WHERE nome = %s", (novo_nome, nome_usuario))
        print(f"✅ Nome alterado para '{novo_nome}'.")
        nome_usuario = novo_nome

    if nova_senha:
        cursor.execute("UPDATE usuarios SET senha = %s WHERE nome = %s", (nova_senha, nome_usuario))
        print("✅ Senha atualizada com sucesso.")

    conn.commit()
    return nome_usuario

def editar_registro_extravio(cursor, conn, usuario_logado):
    # Exibe registros de extravio (ocorrencias + passageiros + voos)
    cursor.execute("""
        SELECT o.id_ocorrencia, p.nome, v.numero_voo
        FROM ocorrencias o
        JOIN bagagens b ON o.id_bagagem = b.id_bagagem
        JOIN passageiros p ON b.id_passageiro = p.id_passageiro
        JOIN voos v ON o.id_voo = v.id_voo
        ORDER BY o.id_ocorrencia
    """)
    registros = cursor.fetchall()
    if not registros:
        print("\nNenhum registro de extravio cadastrado.")
        return usuario_logado
    print("\n--- Registros de Extravio ---")
    for i, reg in enumerate(registros, 1):
        print(f"{i} - Passageiro: {reg[1]} | Voo: {reg[2]}")
    try:
        escolha = int(input("Digite o número do registro que deseja editar (0 para voltar): ").strip())
        if escolha == 0:
            return usuario_logado
        if 1 <= escolha <= len(registros):
            id_ocorrencia = registros[escolha - 1][0]
            cursor.execute("""
                SELECT p.id_passageiro, p.nome, p.email, p.documento, p.data_de_nascimento,
                       v.id_voo, v.numero_voo, v.origem, v.destino, v.horario,
                       pdv.assento, pdv.classe,
                       b.id_bagagem, b.cor, b.marca, b.peso,
                       o.data_hora,
                       COALESCE(d.descricao, ''),
                       COALESCE(e.endereco_entrega, '')
                FROM ocorrencias o
                JOIN bagagens b ON o.id_bagagem = b.id_bagagem
                JOIN passageiros p ON b.id_passageiro = p.id_passageiro
                JOIN voos v ON o.id_voo = v.id_voo
                JOIN passageiros_do_voo pdv ON pdv.id_passageiro = p.id_passageiro AND pdv.id_voo = v.id_voo
                LEFT JOIN danificacao d ON d.id_bagagem = b.id_bagagem
                LEFT JOIN entrega e ON e.id_bagagem = b.id_bagagem
                WHERE o.id_ocorrencia = %s
            """, (id_ocorrencia,))
            dados = cursor.fetchone()
            if not dados:
                print("Registro não encontrado.")
                return usuario_logado

            (id_passageiro, nome, email, documento, data_nasc,
             id_voo, numero_voo, origem, destino, horario,
             assento, classe,
             id_bagagem, cor, marca, peso,
             data_hora, descricao, endereco_entrega) = dados

            print("\n--- Editando Registro ---")
            print("Deixe em branco para manter o valor atual ⚠️.")

            novo_nome = input(f"Novo nome do passageiro [{nome}]: ").strip()
            if novo_nome:
                if novo_nome and all(parte.isalpha() for parte in novo_nome.split()):
                    cursor.execute("UPDATE passageiros SET nome = %s WHERE id_passageiro = %s", (novo_nome, id_passageiro))
                else:
                    print("⚠️ Digite apenas letras e espaços no nome, sem números ou sinais.")
            novo_email = input(f"Novo e-mail [{email}]: ").strip()
            if novo_email:
                if "@" in novo_email and ".com" in novo_email and novo_email.isalnum() == False:
                    cursor.execute("UPDATE passageiros SET email = %s WHERE id_passageiro = %s", (novo_email, id_passageiro))
                else:
                    print("⚠️ E-mail deve conter '@' e '.com'.")
            novo_documento = input(f"Novo documento [{documento}]: ").strip()
            if novo_documento:
                if novo_documento.isdigit() and len(novo_documento) >= 8:
                    cursor.execute("UPDATE passageiros SET documento = %s WHERE id_passageiro = %s", (novo_documento, id_passageiro))
                else:
                    print("⚠️ Documento deve conter apenas números e ter pelo menos 8 dígitos.")
            novo_data_nasc = input(f"Nova data de nascimento [{data_nasc}]: ").strip()
            if novo_data_nasc:
                if (
                    novo_data_nasc
                    and all(c.isdigit() or c == '-' for c in novo_data_nasc)
                    and len(novo_data_nasc.replace("-", "")) >= 8
                ):
                    cursor.execute("UPDATE passageiros SET data_de_nascimento = to_date(%s, 'DD-MM-YYYY') WHERE id_passageiro = %s", (novo_data_nasc, id_passageiro))
                else:
                    print("⚠️ Data de nascimento não pode estar vazia, só pode conter números e traços, e deve ter pelo menos 8 dígitos.")

            novo_numero_voo = input(f"Novo ticket do voo [{numero_voo}]: ").strip()
            if novo_numero_voo:
                if novo_numero_voo.isalnum():
                    cursor.execute("UPDATE voos SET numero_voo = %s WHERE id_voo = %s", (novo_numero_voo, id_voo))
                else:
                    print("⚠️ Número do voo deve ser números e letras ou apenas números.")
            nova_origem = input(f"Nova origem [{origem}]: ").strip()
            if nova_origem:
                if nova_origem.isalpha():
                    cursor.execute("UPDATE voos SET origem = %s WHERE id_voo = %s", (nova_origem, id_voo))
                else:
                    print("⚠️ Origem deve conter apenas letras.")
            novo_destino = input(f"Novo destino [{destino}]: ").strip()
            if novo_destino:
                if novo_destino.isalpha():
                    cursor.execute("UPDATE voos SET destino = %s WHERE id_voo = %s", (novo_destino, id_voo))
                else:
                    print("⚠️ Destino deve conter apenas letras.")
            novo_horario = input(f"Novo horário [{horario}]: ").strip()
            if novo_horario:
                if novo_horario and all(c.isdigit() or c == ':' for c in novo_horario):
                    cursor.execute("UPDATE voos SET horario = %s WHERE id_voo = %s", (novo_horario, id_voo))
                else:
                    print("⚠️ Horário não pode estar vazio e só pode conter números e dois pontos.")

            novo_assento = input(f"Novo assento [{assento}]: ").strip()
            if novo_assento:
                if novo_assento and novo_assento.isalnum():
                    cursor.execute("UPDATE passageiros_do_voo SET assento = %s WHERE id_passageiro = %s AND id_voo = %s", (novo_assento, id_passageiro, id_voo))
                else:
                    print("⚠️ Assento não pode estar vazio e deve conter letras e números.")
            nova_classe = input(f"Nova classe [{classe}]: ").strip()
            if nova_classe:
                if nova_classe and nova_classe.isalpha():
                    cursor.execute("UPDATE passageiros_do_voo SET classe = %s WHERE id_passageiro = %s AND id_voo = %s", (nova_classe, id_passageiro, id_voo))
                else:
                    print("⚠️ Classe não pode estar vazia e deve conter apenas letras.")

            nova_cor = input(f"Nova cor [{cor}]: ").strip()
            if nova_cor:
                if nova_cor.isalpha():
                    cursor.execute("UPDATE bagagens SET cor = %s WHERE id_bagagem = %s", (nova_cor, id_bagagem))
                else:
                    print("⚠️ Digite apenas letras para a cor.")
            nova_marca = input(f"Nova marca [{marca}]: ").strip()
            if nova_marca:
                if nova_marca.isalpha():
                    cursor.execute("UPDATE bagagens SET marca = %s WHERE id_bagagem = %s", (nova_marca, id_bagagem))
                else:
                    print("⚠️ Digite apenas letras para a marca.")
            novo_peso = input(f"Novo peso [{peso}]: ").strip()
            if novo_peso:
                try:
                    peso_float = float(novo_peso)
                    cursor.execute("UPDATE bagagens SET peso = %s WHERE id_bagagem = %s", (peso_float, id_bagagem))
                except ValueError:
                    print("⚠️ Peso deve ser um número (pode ser decimal).")

            nova_data_hora = input(f"Nova data e hora do extravio [{data_hora}]: ").strip()
            if nova_data_hora:
                if nova_data_hora and all(c.isdigit() or c in "- :" for c in nova_data_hora):
                    cursor.execute("UPDATE ocorrencias SET data_hora = to_timestamp(%s, 'DD-MM-YYYY HH24:MI') WHERE id_ocorrencia = %s", (nova_data_hora, id_ocorrencia))
                else:
                    print("⚠️ Data e hora não pode estar vazia e só pode conter números, traços, espaço e dois pontos.")

            nova_descricao = input(f"Nova descrição de danificação [{descricao}]: ").strip()
            if nova_descricao:
                cursor.execute("SELECT id_danificacao FROM danificacao WHERE id_bagagem = %s", (id_bagagem,))
                if cursor.fetchone():
                    cursor.execute("UPDATE danificacao SET descricao = %s WHERE id_bagagem = %s", (nova_descricao, id_bagagem))
                else:
                    cursor.execute("INSERT INTO danificacao (id_bagagem, descricao) VALUES (%s, %s)", (id_bagagem, nova_descricao))

            novo_endereco = input(f"Novo endereço de entrega [{endereco_entrega}]: ").strip()
            if novo_endereco:
                cursor.execute("SELECT id_entrega FROM entrega WHERE id_bagagem = %s", (id_bagagem,))
                if cursor.fetchone():
                    cursor.execute("UPDATE entrega SET endereco_entrega = %s WHERE id_bagagem = %s", (novo_endereco, id_bagagem))
                else:
                    cursor.execute("INSERT INTO entrega (id_bagagem, endereco_entrega) VALUES (%s, %s)", (id_bagagem, novo_endereco))

            conn.commit()
            print("✅ Registro de extravio atualizado com sucesso.")
        else:
            print("Opção inválida.")
    except (ValueError, IndexError):
        print("Opção inválida.")
    return usuario_logado