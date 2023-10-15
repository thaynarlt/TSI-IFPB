from random import randint
from array_ifpb import Array

class PosicaoInvalida(Exception):
    pass

class ListaCheiaException(Exception):
    pass

class ListaVaziaException(Exception):
    pass

class Lista:

    def __init__(self):
        ...

    @property
    def estah_vazia(self) -> bool:
        ...

    @property
    def estah_cheia(self) -> bool:
        ...

    def __len__(self) -> int: # tamanho
        ...

    def __getitem__(self, item): # obter
        ...

    def __contains__(self) -> bool:  # busca
        ...

    def __setitem__(self, item, valor): # modificar
        ...

    def inserir(self, valor):
        ...

    def __del__(self, index): # remover
        ...

    def inserir_inicio(self, valor):
        ...

    def inserir_fim(self, valor):
        ...

    def remover_inicio(self):
        ...

    def remover_fim(self):
        ...

    def __repr__(self):
        ...

    def concatenar(self):
        ...

    def clonar(self):
        ...

    def checar_duplicidade(self):
        ...

    def esvaziar(self):
        ...

    def povoar(self):
        ...


class ListaSequencial:

    def __init__(self):
        self._container = []

    @property
    def estah_vazia(self) -> bool:
        return not self._container

    @property
    def estah_cheia(self) -> bool:
        return False

    def __len__(self) -> int: # tamanho
        return len(self._container)

    def __getitem__(self, item): # obter
        return self._container[item]

    def __contains__(self, item) -> bool:  # busca
        return item in self._container

    def __setitem__(self, index, valor): # modificar
        self._container[index] = valor

    def inserir(self, index, valor):
        self._container.insert(index, valor)

    def __del__(self, index): # remover
        del self._container[index]

    def inserir_inicio(self, valor):
        self._container.insert(0, valor)

    def inserir_fim(self, valor):
        self._container.insert(len(self), valor)

    def remover_inicio(self):
        del self[0]

    def remover_fim(self):
        del self[len(self) - 1]

    def __repr__(self):
        return repr(self)

    def concatenar(self):
        ...

    def clonar(self):
        ...

    def checar_duplicidade(self):
        ...

    def esvaziar(self):
        self._container = []

    def povoar(self):
        ...




class ListaSequencialArray:

    def __init__(self, capacidade=5):
        self._capacidade = capacidade
        self._container = Array(self._capacidade)

    def _obtem_indice(self, index):
        if index < 0:
            return self._capacidade + index
        return index
        
    @property
    def estah_vazia(self) -> bool:
        return not self._container

    @property
    def estah_cheia(self) -> bool:
        return self._container.cheio

    def __len__(self) -> int: # tamanho
        return self._container.tamanho

    def __getitem__(self, index): # obter
        return self._container[self._obtem_indice(index)]

    def __contains__(self) -> bool:  # busca
        ...

    def __setitem__(self, index, valor): # modificar
        index = self._obtem_indice(index)
        if index >= len(self):
            raise PosicaoInvalida("Posicao inexistente")
        self._container[index] = valor

    def _deslocar_a_direita(self, index):
        for i in range(len(self), index, -1):
            self._container[i] = self[i-1]

    def inserir(self, index, valor):
        if self.estah_cheia:
            raise ListaCheiaException()
        
        index = self._obtem_indice(index)
        if index >= len(self):
            self._container[len(self)] = valor
        else:
            self._deslocar_a_direita(index)
            self[index] = valor

    def _deslocar_a_esquerda(self, index):
        for i in range(index, len(self) - 1):
            self[i] = self[i+1]
        print(len(self))
        self._container[len(self)] = None

    def __delitem__(self, index): # remover
        if self.estah_vazia:
            raise ListaVaziaException()
        
        index = self._obtem_indice(index)
        if index >= len(self):
            raise PosicaoInvalida()

        self._deslocar_a_esquerda(index)
        

    def inserir_inicio(self, valor):
        self.inserir(0, valor)

    def inserir_fim(self, valor):
        self.inserir(-1, valor)

    def remover_inicio(self):
        del self[0]

    def remover_fim(self):
        del self[-1]

    def __repr__(self): # equivalente a str
        result = ["["]
    
        for x in range(len(self)):
            result.append(str(self[x]))
            result.append(",")

        if not self.estah_vazia:
            result.pop(-1)

        result.append("]")
        return "".join(result)

    def concatenar(self, segunda_lista):
        for x in range(len(segunda_lista)):
            self.inserir_fim(segunda_lista[x])

    def clonar(self) -> 'ListaSequencialArray':
        nova_lista = ListaSequencialArray()
        for x in range(len(self)):
            nova_lista.inserir_fim(self[x])
        return nova_lista

    def checar_duplicidade(self) -> bool:
        for i in range(len(self)):
            for j in range(i+1, len(self)):
                if self[i] == self[j]:
                    return True
        return False

    def esvaziar(self):
        self._container = Array(capacidade=self._capacidade)

    def povoar(self):
        for x in range(self._capacidade):
            self.inserir(x, randint(0, 10000))


class Node:

    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo: Node | None = proximo


class ListaEncadeada:

    def __init__(self):
        self._inicio: Node | None = None
        self._fim: Node | None = None
        self._tamanho: int = 0

    @property
    def estah_vazia(self) -> bool:
        return self._tamanho == 0

    @property
    def estah_cheia(self) -> bool:
        return False

    def __len__(self) -> int: # tamanho
        return self._tamanho
    
    def _obtem_indice(self, index):
        if index < 0:
            return self._tamanho + index
        return index

    def __getitem__(self, index): # obter
        index = self._obtem_indice(index)
        if not 0 <= index < self._tamanho:
            raise PosicaoInvalida()
        no = self._encontrar_elemento(index)
        return no.valor

    def __contains__(self, item) -> bool:  # busca
        no = self._inicio
        while no:
            if no.valor == item:
                return True
            no = no.proximo
        return False

    def __setitem__(self, index, valor): # modificar
        index = self._obtem_indice(index)
        if not 0 <= index < self._tamanho:
            raise PosicaoInvalida()
        if index == 0:
            self._inicio.valor = valor
        else:
            no = self._encontrar_elemento(index)
            no.valor = valor


    def _encontrar_elemento(self, index):
        no_atual = self._inicio
        posicao = 0
        while posicao < index:
            no_atual = no_atual.proximo
            posicao += 1
        return no_atual

    def inserir(self, index, valor):
        index = self._obtem_indice(index)
        node = Node(valor)
        if self.estah_vazia:
            self._inicio = self._fim = node
        elif index == 0:
            node.proximo = self._inicio
            self._inicio = node
        elif index >= len(self):
            self._fim.proximo = node
            self._fim = node
        else:
            predecessor = self._encontrar_elemento(index - 1)
            node.proximo = predecessor.proximo
            predecessor.proximo = node

        self._tamanho += 1

    def __delitem__(self, index): # remover
        if self.estah_vazia:
            raise ListaVaziaException()
        elif index == 0:
            self._inicio = self._inicio.proximo
        else:
            predecessor = self._encontrar_predecessor(index)
            predecessor.proximo = predecessor.proximo.proximo

        self._tamanho -= 1

    def inserir_inicio(self, valor):
        self.inserir(0, valor)

    def inserir_fim(self, valor):
        self.inserir(len(self), valor)

    def remover_inicio(self):
        del self[0]

    def remover_fim(self):
        del self[-1]

    def __repr__(self):
        result = ["["]
    
        no = self._inicio
        while no != None:
            result.append(str(no.valor))
            result.append(",")
            no = no.proximo

        if not self.estah_vazia:
            result.pop(-1)

        result.append("]")
        return "".join(result)

    def concatenar(self):
        ...

    def clonar(self):
        ...

    def checar_duplicidade(self):
        ...

    def esvaziar(self):
        ...

    def povoar(self):
        ...

