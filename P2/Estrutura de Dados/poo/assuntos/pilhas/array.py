

class Array:

    def __init__(self, tamanho):
        self.__quantidade_elementos = 0
        self.__tamanho = tamanho
        self.__dados = [None] * tamanho

    @property
    def vazio(self):
        return self.__quantidade_elementos == 0
    
    @property
    def cheio(self):
        return self.__quantidade_elementos == self.__tamanho
    
    def set(self, posicao, valor):
        self.__dados[posicao] = valor
        self.__quantidade_elementos += 1

    __setitem__ = set

    def get(self, posicao):
        return self.__dados[posicao]
    
    __getitem__ = get
    
    def delete(self, posicao):
        self.__dados[posicao] = None
        self.__quantidade_elementos -= 1

    __delitem__ = delete
    
    @property
    def tamanho(self):
        return self.__quantidade_elementos
    
    def __len__(self):
        return self.tamanho
    
    @property
    def tamanho_total(self):
        return self.__tamanho
    


if __name__ == "__main__":
    a = Array(10)
    assert len(a) == 0
    a[0] = "alguma coisa"
    assert len(a) == 1
    assert a[0] == "alguma coisa"
    a.delete(0)
    assert len(a) == 0
    assert a[0] == None
    a[1] = "outra coisa"
    assert len(a) == 1
    del a[1]
    assert len(a) == 0
