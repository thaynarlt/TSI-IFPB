from array_ifpb import Array

class FilaCheiaException(Exception):
    pass
class FilaVaziaException(Exception):
    pass

class Node:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo: Node | None = proximo
    
    def __repr__(self):
        return f'Node(valor={self.valor})'

class FilaSequencialArray:
    def __init__(self):
        self.__dados = Array(5)
        self.__inicio = 0
        self.__fim = 0
        self.__tamanho = 0

    @property #uma forma de encapsular um atributo e seu getter e setter
    def inicio(self):
        #a fila é circular
        return self.__inicio % self.__dados.capacidade #retorna o índice do primeiro elemento da fila

    @property #uma forma de encapsular um atributo e seu getter e setter
    def fim(self):
        return self.__fim % self.__dados.capacidade #o índice do próximo elemento a ser inserido na fila

    def tamanho(self) -> int: #retorna tamanho da fila
        return self.__tamanho
    
    def estaVazia(self) -> bool: #retorna se está vazia ou não
        return self.tamanho() == 0
    
    def enfileirar(self,valor):
        if self.__tamanho == self.__dados.capacidade:
            raise FilaCheiaException()
        self.__dados[self.fim] = valor #atribui um valor ao final da fila
        self.__fim +=1 # incrementa o índice do próximo elemento a ser inserido na fila
        #Como a fila é circular, o índice do próximo elemento é calculado como self.__fim % self.__dados.capacidade
        self.__tamanho+=1 #aumenta o tamanho da fila

    def desenfileirar(self):
        if self.estaVazia():
            raise FilaVaziaException()
        posicao = self.inicio
        valor = self.__dados[posicao]
        del self.__dados[posicao]
        self.__inicio +=1
        self.__tamanho -=1
        return valor
    
    def __str__(self) -> str: #isso aqui é um quebra-cabeça
        r = "["
        for x in range(self.__inicio, self.__fim):
            r += f"{self.__dados[x % self.__dados.capacidade]}, "
        
        if self.tamanho():
            r = r[:-2] 
        r += "]"
        return r