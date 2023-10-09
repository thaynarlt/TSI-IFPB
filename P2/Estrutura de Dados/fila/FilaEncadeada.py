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

    def tamanho(self) -> int:
        return self.__tamanho
    
    def estaVazia(self) -> bool:
        return self.tamanho() == 0
