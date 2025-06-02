def excluir(cursor, conn, usuario_logado):
    print("\n-- Excluir Usuário --")

    if usuario_logado == "admin":
        nome = input("Digite o nome do usuário que deseja excluir: ").strip().lower()
        cursor.execute("SELECT nome FROM usuarios WHERE LOWER(nome) = %s", (nome,))
        usuario_alvo = cursor.fetchone()
        if not usuario_alvo:
            print("❌ Usuário não encontrado.")
            return usuario_logado
        if nome == "admin":
            print("⚠️ O administrador não pode excluir sua própria conta.")
            return usuario_logado
    else:
        nome = usuario_logado
        cursor.execute("SELECT nome FROM usuarios WHERE nome = %s", (nome,))
        usuario_alvo = cursor.fetchone()

    confirmacao = input(f"Tem certeza que deseja excluir '{nome}'? (s/n): ").lower()
    if confirmacao == "s" or confirmacao == "sim":
        cursor.execute("DELETE FROM usuarios WHERE nome = %s", (nome,))
        conn.commit()
        print(f"✅ Usuário '{nome}' excluído com sucesso.")
        if nome == usuario_logado:
            return None

    return usuario_logado

def excluir_registro_extravio(cursor, conn, usuario_logado):
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
        while True:
            escolha = input("Digite o número do registro que deseja excluir (0 para voltar): ").strip()
            if escolha and escolha.isdigit():
                escolha = int(escolha)
                break
            print("Digite um número válido.")
        if escolha == 0:
            return usuario_logado
        if 1 <= escolha <= len(registros):
            while True:
                confirmacao = input(f"Tem certeza que deseja excluir o registro {escolha}? (s/n): ").strip().lower()
                if confirmacao and confirmacao.isalpha():
                    break
                print("Confirmação deve ser uma resposta de sim ou não (s/n).")
            if confirmacao == "s" or confirmacao == "sim":
                id_ocorrencia = registros[escolha - 1][0]
                cursor.execute("SELECT id_bagagem FROM ocorrencias WHERE id_ocorrencia = %s", (id_ocorrencia,))
                id_bagagem = cursor.fetchone()[0]
                cursor.execute("DELETE FROM danificacao WHERE id_bagagem = %s", (id_bagagem,))
                cursor.execute("DELETE FROM entrega WHERE id_bagagem = %s", (id_bagagem,))
                cursor.execute("DELETE FROM ocorrencias WHERE id_ocorrencia = %s", (id_ocorrencia,))
                cursor.execute("DELETE FROM bagagens WHERE id_bagagem = %s", (id_bagagem,))
                conn.commit()
                print(f"✅ Registro do passageiro '{registros[escolha - 1][1]}' excluído com sucesso.")
            else:
                print("Operação cancelada.")
        else:
            print("Opção inválida.")
    except (ValueError, IndexError):
        print("Opção inválida.")

    return usuario_logado