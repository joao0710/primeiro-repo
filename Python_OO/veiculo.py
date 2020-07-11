import abc

class Veiculo(abc.ABC):
    def __init__(self, cor, tipo_combustivel, potencia):
        self.__cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia

    @property
    def cor(self):
        return self.__cor

    @porperty
    def tipo_combustivel(self):
        return self.__tipo_combustivel

    @property
    def potencia(self):
        return self.__potencia

    def pintar(self, cor):
        self.__cor = cor

