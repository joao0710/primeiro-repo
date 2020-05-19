
#IMPRIMIR UMA PALAVRA INSERIDA INVERTIDAMENTE
if __name__ == "__main__":

    palavra = input()

    for index in range(len(palavra) - 1, -1, -1):
      print(palavra[index], end='')