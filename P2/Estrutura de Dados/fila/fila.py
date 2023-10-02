from array_ifpb import Array

class FilaException(Exception):
    pass

class FilaVaziaException(FilaException):
    pass

class FilaCheiaException(FilaException):
    pass

class Fila:
    def __init__(self):
        ...

    def tamanho(self):
        ...

    def estah_vazia(self):
        ...

    def enfileirar(self, valor):
        ...

    def desenfileirar(self):
        ...

    def __str__(self):
        ...

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
    

class FilaSequencial:

    def __init__(self):
        self.__dados = Array(5)
        self.__inicio = 0
        self.__fim = 0
        self.__tamanho = 0

    @property
    def inicio(self):
        return self.__inicio % self.__dados.capacidade
    
    @property
    def fim(self):
        return self.__fim % self.__dados.capacidade

    def tamanho(self) -> int:
        return self.__tamanho

    def estah_vazia(self) -> bool:
        return self.tamanho() == 0

    def enfileirar(self, valor):
        if self.__tamanho == self.__dados.capacidade:
            raise FilaCheiaException()
        
        self.__dados[self.fim] = valor
        self.__fim += 1
        self.__tamanho += 1

    def desenfileirar(self):
        if self.estah_vazia():
            raise FilaVaziaException()
        posicao = self.inicio
        valor = self.__dados[posicao]
        del self.__dados[posicao]
        self.__inicio += 1
        # self._deslocar_a_esquerda()
        self.__tamanho -= 1
        return valor

    # def _deslocar_a_esquerda(self, posicao=0):
    #     while self.__dados[posicao + 1] != None:  # deslocar a esquerda
    #         self.__dados[posicao] = self.__dados[posicao+1]
    #         posicao += 1
    #     self.__dados[posicao] = None

    def __str__(self) -> str:
        r = "["
        for x in range(self.__inicio, self.__fim):
            r += f"{self.__dados[x % self.__dados.capacidade]}, "
        
        if self.tamanho():
            r = r[:-2] 
        r += "]"
        return r
    

class Node:
    
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo: Node | None = proximo

    def __repr__(self):
        return f'Node(valor={self.valor})'
    

class FilaEncadeada:
    
    def __init__(self):
        self.__inicio: Node | None = None
        self.__fim: Node | None = None
        self.__tamanho: int = 0

    def tamanho(self) ->int :
        return self.__tamanho

    def estah_vazia(self) -> bool:
        return self.tamanho() == 0

    def enfileirar(self, valor) -> None:
        elemento = Node(valor)
        if self.estah_vazia():
            self.__inicio = elemento
        else:
            self.__fim.proximo = elemento

        self.__fim = elemento
        self.__tamanho += 1

    def desenfileirar(self):
        if self.estah_vazia():
            raise FilaVaziaException()

        valor = self.__inicio.valor
        self.__inicio = self.__inicio.proximo
        self.__tamanho -= 1
        return valor
    
    def busca(self, valor) -> bool:
        no = self.__inicio
        while no != None:
            if no.valor == valor:
                return True
            no = no.proximo
        return False
    
    def __contains__(self, valor):
        return self.busca(valor)

    def __str__(self):
        result = ["["]
    
        no = self.__inicio
        while no != None:
            result.append(str(no.valor))
            result.append(",")
            no = no.proximo

        if not self.estah_vazia():
            result.pop(-1)

        result.append("]")
        return "".join(result)