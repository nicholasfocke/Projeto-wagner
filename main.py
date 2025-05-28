import os
from menu import menu_geral, menu_logado
from login import login
from cadastro import cadastrar
from exibir import exibir, exibir_registros
from editar import editar, editar_registro_extravio
from excluir import excluir, excluir_registro_extravio
from validacoes import nome_valido, senha_valida
from registro_extravio import coletar_dados_passageiro, coletar_dados_voo, coletar_dados_passageiro_voo, coletar_dados_bagagem, coletar_ocorrencia, coletar_danificacao, coletar_entrega, formulario_completo, registros_extravio


def main():
    usuarios = [{"nome": "admin", "senha": "admin123"}]
    usuario_logado = None

    while True:
        if usuario_logado:
            menu_logado(usuario_logado)
            opcao = input("Escolha uma opção: ").strip()
            os.system('cls')

            if opcao == "1":
                exibir(usuarios)

            elif opcao == "2":
                usuario_logado = editar(usuarios, usuario_logado)

            elif opcao == "3":
                usuario_logado = excluir(usuarios, usuario_logado)

            elif opcao == "4":
                usuario_logado = formulario_completo(usuario_logado)

            elif opcao == "5":
                usuario_logado = exibir_registros(usuario_logado)

            elif opcao == "6":
                usuario_logado = excluir_registro_extravio(registros_extravio, usuario_logado)
            
            elif opcao == "7":
                usuario_logado = editar_registro_extravio(registros_extravio, usuario_logado)

            elif opcao == "0":
                print("👋 Logout realizado com sucesso!")
                usuario_logado = None

            else:
                print("⚠️ Opção inválida! Tente novamente.")
            
        else:
            menu_geral()
            opcao = input("Escolha uma opção: ").strip()
            os.system('cls')

            if opcao == "1":
                usuario_logado = login(usuarios)

            elif opcao == "2":
                cadastrar(usuarios)

            elif opcao == "3":
                print("👋 Programa encerrado. Até logo!")
                break

            else:
                print("⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()