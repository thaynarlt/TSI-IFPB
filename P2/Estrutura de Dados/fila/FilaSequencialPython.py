class FilaException(Exception):
    pass

class FilaVaziaException(FilaException):
    pass


class FilaSequencialPython:

    def __init__(self):
        self.__dados = []

    def tamanho(self):
        return len(self.__dados)
    
    def estah_vazia(self):
        return self.tamanho() == 0

    def enfileirar(self, valor):
        self.__dados.append(valor)

    def desenfileirar(self):
        if self.estah_vazia():
            raise FilaVaziaException()
        return self.__dados.pop(0)

    def __str__(self):
        return str(self.__dados)