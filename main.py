import os
from menu import menu_geral, menu_logado
from login import login
from cadastro import cadastrar
from exibir import exibir
from editar import editar
from excluir import excluir
from validacoes import nome_valido, senha_valida


def main():
    usuarios = {"admin": "admin123"}
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