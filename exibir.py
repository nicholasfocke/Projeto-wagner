from registro_extravio import registros_extravio

def exibir(usuarios):
    print('\n--Lista de usuários--')
    if not usuarios:
        print("📭 Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"- Nome: {usuario['nome']}")

def exibir_registros(usuario_logado):
    if not registros_extravio:
        print("\nNenhum registro de extravio cadastrado.")
        return usuario_logado
    
    print("\n--- Registros de Extravio ---")
    for i, registro in enumerate(registros_extravio, 1):
        print(f"{i} - Passageiro: {registro['Passageiro']['nome']} | Voo: {registro['Voo']['numero_voo']}")

    try:
        escolha = int(input("Digite o número do registro para ver detalhes (0 para voltar): "))
        if escolha == 0:
            return usuario_logado
        registro = registros_extravio[escolha - 1]
        print("\n--- Detalhes do Registro ---")
        for chave, valor in registro.items():
            print(f"{chave}:")
            if isinstance(valor, dict):
                for subchave, subvalor in valor.items():
                    print(f"  {subchave}: {subvalor}")
            else:
                print(f"  {valor}")

    except (ValueError, IndexError):
        print("Opção inválida.")

    return usuario_logado