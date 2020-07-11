from contato import Contato
from arquivo_service import *

print("-" * 30)
print(("-" *3) + " Agenda de contatos TW " + ("-" *3))
print("-" * 30)

opcao_menu = 1

while(opcao_menu != 0):
    print("1. Listar contatos")
    print("2. Cadastrar contato")
    print("3. Remover contato")
    print("4. Buscar contato")
    print("0. Sair")
    opcao_menu = int(input("Digite a opção desejada: "))

    if opcao_menu == 1:
        contatos = listar_contato()
        for contato in contatos:
            print(f'nome: {contato.nome} / {contato.email} / {contato.telefone}')
    elif opcao_menu == 2:
        nome_contato = input("Digite o nome do contato: ")
        email_contato = input("Digite o email do contato: ")
        telefone_contato = input("Digite o telefone do contato: ")
        contato_novo = Contato(nome_contato, email_contato, telefone_contato)
        cadastrar_contato(contato_novo)
    elif opcao_menu == 3:
        contato_remover = input("Digite o e-mail do contato que desejas remover: ")
        contato_removido = remover_contato_email(contato_remover)
        if contato_removido:
            print("Contato removido com sucesso")
        else:
            print("Nenhum contato removido")

    elif opcao_menu == 4:
        contato_buscar = input("Digite o e-mail do contato que desejas buscar")
        contato_encontrado = buscar_contato_email(contato_buscar)
        if contato_encontrado:
            print(f'nome: {contato_encontrado.nome} / {contato_encontrado.email} / {contato_encontrado.telefone}')
        else:
            print('Contato não encontrado')


    else:
        print("opcao invalida")
else:
    print("Obrigado por usar a agenda de contatos TW")