registros_extravio = []

def coletar_dados_passageiro():
    print("\n--- Dados do Passageiro ---")
    while True:
        nome = input("Nome completo: ").strip()
        if nome and all(parte.isalpha() for parte in nome.split()):
            break
        print("⚠️ Digite apenas letras e espaços no nome, sem números ou sinais.")
    while True:
        email = input("E-mail: ").strip()
        if "@" in email and ".com" in email and email.isalnum() == False:
            break
        print("⚠️ E-mail deve conter '@' e '.com'.")
    while True:
        documento = input("Documento (RG/CPF/Passaporte): ").strip()
        if documento.isdigit() and len(documento) >= 8:
            break
        print("⚠️ Documento deve conter apenas números e ter pelo menos 8 dígitos.")
    while True:
        data_nascimento = input("Data de nascimento (DD-MM-AAAA): ").strip()
        if (
            data_nascimento
            and all(c.isdigit() or c == '-' for c in data_nascimento)
            and len(data_nascimento.replace("-", "")) >= 8
        ):
            break
        print("⚠️ Data de nascimento não pode estar vazia, só pode conter números e traços, e deve ter pelo menos 8 dígitos.")
    return {
        "nome": nome,
        "email": email,
        "documento": documento,
        "data_nascimento": data_nascimento
    }

def coletar_dados_voo():
    print("\n--- Dados do Voo ---")
    while True:
        numero_voo = input("Ticket do voo: ").strip()
        if numero_voo.isalnum():
            break
        print("⚠️ Número do voo deve ser números e letras ou apenas números.")
    while True:
        origem = input("Origem: ").strip()
        if origem.isalpha():
            break
        print("⚠️ Origem deve conter apenas letras.")
    while True:
        destino = input("Destino: ").strip()
        if destino.isalpha():
            break
        print("⚠️ Destino deve conter apenas letras.")
    while True:
        horario = input("Horário (HH:MM): ").strip()
        if horario and all(c.isdigit() or c == ':' for c in horario):
            break
        print("⚠️ Horário não pode estar vazio e só pode conter números e dois pontos.")
    return {
        "numero_voo": numero_voo,
        "origem": origem,
        "destino": destino,
        "horario": horario
    }

def coletar_dados_passageiro_voo():
    print("\n--- Dados do Passageiro no Voo ---")
    while True:
        assento = input("Assento: ").strip()
        if assento and assento.isalnum():
            break
        print("⚠️ Assento não pode estar vazio e deve conter letras e números.")
    while True:
        classe = input("Classe (Econômica/Executiva/Primeira): ").strip()
        if classe and classe.isalpha():
            break
        print("⚠️ Classe não pode estar vazia e deve conter apenas letras.")
    return {
        "assento": assento,
        "classe": classe
    }

def coletar_dados_bagagem():
    print("\n--- Dados da Bagagem ---")
    while True:
        cor = input("Cor da bagagem: ").strip()
        if cor.isalpha():
            break
        print("⚠️ Digite apenas letras para a cor.")
    while True:
        marca = input("Marca da bagagem: ").strip()
        if marca.isalpha():
            break
        print("⚠️ Digite apenas letras para a marca.")
    while True:
        peso = input("Peso (kg): ").strip()
        try:
            peso = float(peso)
            break
        except ValueError:
            print("⚠️ Peso deve ser um número (pode ser decimal).")
    return {
        "cor": cor,
        "marca": marca,
        "peso": peso
    }

def coletar_ocorrencia():
    print("\n--- Dados da Ocorrência ---")
    while True:
        data_hora = input("Data e hora do extravio (DD-MM-AAAA HH:MM): ").strip()
        if data_hora and all(c.isdigit() or c in "- :"
                             for c in data_hora):
            break
        print("⚠️ Data e hora não pode estar vazia e só pode conter números, traços, espaço e dois pontos.")
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
    print("\n ✅ Registro concluído e salvo na memória.")

    return usuario_logado
