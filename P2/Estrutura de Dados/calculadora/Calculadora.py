class Calculadora:
    def __init__(self):
        self.__registrador = 0
        self.__valor_anterior = 0
   
    @property
    def registrador(self) -> float:
        return self.__registrador
    
    @registrador.setter
    def registrador(self, valor: float):
        self.__registrador = valor

    def somar(self, valor: float):
        self.__valor_anterior = self.__registrador
        self.__registrador += valor      

    def subtrair(self, valor: float):
        self.__valor_anterior = self.__registrador
        self.__registrador -= valor

    def dividir(self, valor: float):
        self.__valor_anterior = self.__registrador
        self.__registrador = self.__registrador / valor
    
    def multiplicar(self, valor: float):
        self.__valor_anterior = self.__registrador
        self.__registrador = self.__registrador * valor

    def resetar(self):
        self.__valor_anterior = self.__registrador
        self.__registrador = 0
    
    def desfazer(self):
        self.__registrador = self.__valor_anterior

    def __str__(self):
        return f'Registrador: {self.__registrador}'