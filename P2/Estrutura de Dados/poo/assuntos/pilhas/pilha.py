
class PilhaException(Exception):
    pass

    
class Pilha:

    def __init__(self):
        ...

    def esta_vazia(self):
        ...

    def tamanho(self):
        ...

    def empilhar(self, elemento):
        ...

    def desempilhar(self):
        ...

    def imprimir(self):
        ...
    
    def __str__(self):
        ...


class PilhaSequencial:

    def __init__(self):
        self._dados = []

    def esta_vazia(self):
        return self.tamanho() == 0

    def tamanho(self):
        return len(self._dados)

    def empilhar(self, elemento):
        self._dados.append(elemento)

    def desempilhar(self):
        if self.esta_vazia():
            raise PilhaException()
            
        return self._dados.pop()

    def imprimir(self):
        print(self._dados)
    
    def __str__(self):
        return f'Pilha()'