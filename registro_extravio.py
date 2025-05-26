registros_extravio = []

def coletar_dados_passageiro():
    print("\n--- Dados do Passageiro ---")
    nome = input("Nome completo: ").strip()
    email = input("E-mail: ").strip()
    documento = input("Documento (RG/CPF/Passaporte): ").strip()
    data_nascimento = input("Data de nascimento (AAAA-MM-DD): ").strip()
    return {
        "nome": nome,
        "email": email,
        "documento": documento,
        "data_nascimento": data_nascimento
    }

def coletar_dados_voo():
    print("\n--- Dados do Voo ---")
    numero_voo = input("Número do voo: ").strip()
    origem = input("Origem: ").strip()
    destino = input("Destino: ").strip()
    horario = input("Horário (HH:MM): ").strip()
    return {
        "numero_voo": numero_voo,
        "origem": origem,
        "destino": destino,
        "horario": horario
    }

def coletar_dados_passageiro_voo():
    print("\n--- Dados do Passageiro no Voo ---")
    assento = input("Assento: ").strip()
    classe = input("Classe (Econômica/Executiva/Primeira): ").strip()
    return {
        "assento": assento,
        "classe": classe
    }

def coletar_dados_bagagem():
    print("\n--- Dados da Bagagem ---")
    cor = input("Cor da bagagem: ").strip()
    marca = input("Marca da bagagem: ").strip()
    peso = input("Peso (kg): ").strip()
    return {
        "cor": cor,
        "marca": marca,
        "peso": peso
    }

def coletar_ocorrencia():
    print("\n--- Dados da Ocorrência ---")
    data_hora = input("Data e hora do extravio (AAAA-MM-DD HH:MM): ").strip()
    return {
        "data_hora": data_hora
    }

def coletar_danificacao():
    print("\n--- Danificação (se houver) ---")
    descricao = input("Descrição da danificação (deixe em branco se não houver): ").strip()
    return {
        "descricao": descricao
    }

def coletar_entrega():
    print("\n--- Endereço para Entrega da Bagagem (se aplicável) ---")
    endereco = input("Endereço completo para entrega (deixe em branco se não houver): ").strip()
    return {
        "endereco_entrega": endereco
    }

def formulario_completo(usuario_logado):
    print("=== Formulário de Extravio de Bagagem ===")
    passageiro = coletar_dados_passageiro()
    voo = coletar_dados_voo()
    passageiro_voo = coletar_dados_passageiro_voo()
    bagagem = coletar_dados_bagagem()
    ocorrencia = coletar_ocorrencia()
    danificacao = coletar_danificacao()
    entrega = coletar_entrega()

    registro = {
        "Passageiro": passageiro,
        "Voo": voo,
        "Passageiro no Voo": passageiro_voo,
        "Bagagem": bagagem,
        "Ocorrência": ocorrencia,
        "Danificação": danificacao,
        "Entrega": entrega
    }
    registros_extravio.append(registro)

    print("\n--- Resumo do Registro de Extravio ---")
    for chave, valor in registro.items():
        print(f"{chave}: {valor}")
    print("\nRegistro concluído e salvo na memória.")

    return usuario_logado
