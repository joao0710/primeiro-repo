import veiculo

class Carro(veiculo.Veiculo):
    def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
        super().__init__(cor, tipo_combustivel,potencia)
        self.__qtd_portas = qtd_portas

    @property
    def qtd_portas(self):
        return  self.__qtd_portas

