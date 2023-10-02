

class Array:

    def __init__(self, capacidade: int):
        self.__quantidade_elementos = 0
        self.__capacidade = capacidade
        self.__dados = [None] * capacidade

    @property
    def vazio(self) -> bool:
        return self.__quantidade_elementos == 0
    
    @property
    def cheio(self) -> bool:
        return self.__quantidade_elementos == self.__capacidade
    
    def set(self, posicao, valor) -> None:
        if valor is None:
            if self.__dados[posicao]:
                self.__quantidade_elementos -= 1    
        else:
            self.__quantidade_elementos += 1
        
        self.__dados[posicao] = valor
    
    __setitem__ = set

    def get(self, posicao):
        return self.__dados[posicao]
    
    __getitem__ = get
    
    def delete(self, posicao) -> None:
        self.__dados[posicao] = None
        self.__quantidade_elementos -= 1

    __delitem__ = delete
    
    @property
    def tamanho(self) -> int:
        return self.__quantidade_elementos
    
    def __len__(self):
        return self.tamanho
    
    @property
    def capacidade(self) -> int:
        return self.__capacidade
    
    def copiar_de(self, outro: 'Array'):
        for x in range(outro.tamanho):
            self[x] = outro[x]
    


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
    assert a[3] == None
    a[3] = None
    assert len(a) == 0
    a[3] = "abacaxi"
    assert len(a) == 1
    assert a[3] == "abacaxi"
    a[3] = None
    assert len(a) == 0
