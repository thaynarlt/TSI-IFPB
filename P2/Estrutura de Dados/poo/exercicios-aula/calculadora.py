
class CalculadoraErro(Exception):
    pass

    
class Calculadora:

    def __init__(self):
        self._registrador = 0
        self._valores = []

    def _guarda_registrador(self):
        self._valores.append(self._registrador)

    def get_registrador(self):
        return self._registrador

    def adicionar(self, valor):
        self._guarda_registrador()
        self._registrador += valor

    def subtrair(self, valor):
        self._guarda_registrador()
        self._registrador -= valor

    def multiplicar(self, valor):
        self._guarda_registrador()
        self._registrador *= valor

    def dividir(self, valor):
        self._guarda_registrador()
        try:
            self._registrador /= valor
        except ZeroDivisionError:
            raise CalculadoraErro

    def exibe(self):
        print(self.get_registrador())

    def reset(self):
        self._registrador = 0

    def desfazer(self):
        self._registrador = self._valores.pop()

    def __str__(self):
        return f"Calculadora({self._registrador})"