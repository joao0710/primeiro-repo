from usuario import Usuario


continuar = 1
lista_usuario = []

while continuar != 0:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sobrenome = input("Digite seu sobrenome: ")

    usuario = Usuario(nome, idade, sobrenome)

    lista_usuario.append(usuario)

    continuar = int(input("Deseja continuar? 0 - Sair  // 1 - Continuar"))

else:
    print("Lista de usuários: ")
    for x in lista_usuario:
        print(f'Nome: {x.nome} {x.sobrenome} - Idade: {x.idade}')