#NÓ
class Node:
    def __init__(self, valor:int):
        self._valor: int = valor
        self.filho_esquerda: None | Node = None
        self.filho_direita: None | Node = None

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, novo_valor):
        self._valor = novo_valor
    
    def add_esquerda(self, valor: int):
        if not self.filho_esquerda:
            self.filho_esquerda = Node(valor)
        else:
            self.filho_esquerda.add_esquerda(valor)
    
    def add_direita(self,valor: int):
        if not self.filho_direita:
            self.filho_direita = Node(valor)
        else:
            self.filho_direita.add_direita(valor)

    @property
    def tem_filho_direita(self) -> bool:
        return self.filho_direita is not None
    
    @property
    def tem_filho_esquerda(self) -> bool:
        return self.filho_esquerda is not None
    
    @property
    def eh_folha(self) -> bool:
        return self.filho_direita is None and self.filho_esquerda is None
    
#Árvore Binária de Busca:
class abb:

    def __init__(self):
        self._raiz: Node | None = None

#INSERÇÃO NA ABB:   
    def add(self,valor):
        self._raiz = self._add(self._raiz, valor)

    def _add(self, no: Node, valor):
        if no is None:
            return Node(valor)
        else:
            if valor > no.valor:
                no.filho_direita = self._add(no.filho_direita,valor)
            else:
                no.filho_esquerda = self._add(no.filho_esquerda,valor)
            return no
        
#REMOÇÃO NA ABB:
    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)
        
    def _remover(self, node: Node, valor: int):
        if node is None:
            return node
        
        if valor < node.valor:
            node.filho_esquerda = self._remover(node.filho_esquerda, valor)
        elif valor > node.valor:
            node.filho_direita = self._remover(node.filho_direita, valor)
        else:
            if not node.tem_filho_esquerda:
                return node.filho_direita
            elif not node.tem_filho_direita:
                return node.filho_esquerda
            else:
                substituto = self.no_maior_valor(node.filho_esquerda)
                node.valor = substituto.valor
                node.filho_esquerda = self._remover(
                    node.filho_esquerda,
                    substituto.valor
                )
        return node