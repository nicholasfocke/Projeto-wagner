def exibir(cursor):
    print('\n--Lista de usuários--')
    cursor.execute("SELECT nome FROM usuarios ORDER BY nome")
    usuarios = cursor.fetchall()
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"- Nome: {usuario[0]}")

def exibir_registros(cursor, usuario_logado):
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
        escolha = int(input("Digite o número do registro para ver detalhes (0 para voltar): "))
        if escolha == 0:
            return usuario_logado
        id_ocorrencia = registros[escolha - 1][0]
        cursor.execute("""
            SELECT p.nome, p.email, p.documento, p.data_de_nascimento,
                   v.numero_voo, v.origem, v.destino, v.horario,
                   pdv.assento, pdv.classe,
                   b.cor, b.marca, b.peso,
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
        detalhes = cursor.fetchone()
        if detalhes:
            print("\n--- detalhes do Registro ---")
            print("Passageiro:")
            print(f"  Nome: {detalhes[0]}")
            print(f"  Email: {detalhes[1]}")
            print(f"  Documento: {detalhes[2]}")
            print(f"  Data de Nascimento: {detalhes[3]}")
            print("Voo:")
            print(f"  Número do Voo: {detalhes[4]}")
            print(f"  Origem: {detalhes[5]}")
            print(f"  Destino: {detalhes[6]}")
            print(f"  Horário: {detalhes[7]}")
            print("Passageiro no Voo:")
            print(f"  Assento: {detalhes[8]}")
            print(f"  Classe: {detalhes[9]}")
            print("Bagagem:")
            print(f"  Cor: {detalhes[10]}")
            print(f"  Marca: {detalhes[11]}")
            print(f"  Peso: {detalhes[12]}")
            print("Ocorrência:")
            print(f"  Data e Hora: {detalhes[13]}")
            print("Danificação:")
            print(f"  Descrição: {detalhes[14]}")
            print("Entrega:")
            print(f"  Endereço: {detalhes[15]}")
        else:
            print("Registro não encontrado.")

    except (ValueError, IndexError):
        print("Opção inválida.")

    return usuario_logado