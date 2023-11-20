class Node:

    def __init__(self, valor: int):
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

    def add_direita(self, valor: int):
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

    

class Arvore:

    def __init__(self):
        self._raiz: Node | None = None

    @property
    def esta_vazia(self) -> bool:
        return self._raiz is None
    
    @property
    def raiz(self) -> Node | None:
        return self._raiz
    
    @raiz.setter
    def raiz(self, valor):
        self._raiz = valor

    def add(self, valor):
        self._raiz = self._add(self.raiz, valor)

    def _add(self, no: Node, valor):
        if no is None:
            return Node(valor)
        else:
            if valor > no.valor:
                no.filho_direita = self._add(no.filho_direita, valor)
            else:
                no.filho_esquerda = self._add(no.filho_esquerda, valor)
            return no
        
    def percorrer_esquerdo(self):
        if self.raiz:
            self._percorrer_em_ordem(self.raiz.filho_esquerda)

    def percorrer(self):
        self._percorrer_em_ordem(self.raiz)

    def _percorrer_pre_ordem(self, no: Node | None):
        if not no:
            return
        print(no.valor)
        self._percorrer_pre_ordem(no.filho_esquerda)
        self._percorrer_pre_ordem(no.filho_direita)

    def _percorrer_em_ordem(self, no: Node | None):
        if not no:
            return
        
        self._percorrer_em_ordem(no.filho_esquerda)
        print(no.valor)
        self._percorrer_em_ordem(no.filho_direita)

    def _percorrer_pos_ordem(self, no: Node | None):
        if not no:
            return

        self._percorrer_pos_ordem(no.filho_esquerda)
        self._percorrer_pos_ordem(no.filho_direita)
        print(no.valor)

    @property
    def altura(self) -> int:
        return self._get_altura(self.raiz)
    
    def _get_altura(self, no: Node | None) -> int:
        if not no:
            return 0
        alt_esquerda = self._get_altura(no.filho_esquerda)
        alt_direita = self._get_altura(no.filho_direita)
        return 1 + max(alt_esquerda, alt_direita)
    
    @property
    def total_nos(self) -> int:
        return self._get_total_nos(self.raiz)
    
    def _get_total_nos(self, no: Node| None) -> int:
        if not no:
            return 0
        return 1 +\
              self._get_total_nos(no.filho_esquerda) +\
                  self._get_total_nos(no.filho_direita)
    
    def no_menor_valor(self, node: Node):
        atual = node
        while atual.tem_filho_esquerda:
            atual = atual.filho_esquerda
        return atual
    
    def no_maior_valor(self, node: Node):
        atual = node
        while atual.tem_filho_direita:
            atual = atual.filho_direita
        return atual
    
    def remover(self, valor):
        self.raiz = self._remover(self.raiz, valor)
    
    def _remover(self, node: Node, valor: int):
        if node is None:
            return node
        
        if valor < node.valor:
            node.filho_esquerda = self._remover(node.filho_esquerda, valor)
        elif valor > node.valor:
            node.filho_direita = self._remover(node.filho_direta, valor)
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
    
    def busca(self, valor) -> bool:
        return self._busca(self.raiz, valor)

    def _busca(self, no: Node, valor, nivel=0) -> bool:
        if no is None:
            return (False, nivel)
        elif valor == no.valor:
            return (True, nivel)
        elif valor > no.valor:
            return self._busca(no.filho_direita, valor, nivel+1)
        else:
            return self._busca(no.filho_esquerda, valor, nivel+1)

    

    
