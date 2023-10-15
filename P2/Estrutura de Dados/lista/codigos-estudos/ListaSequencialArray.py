from random import randint
from array_ifpb import Array

class PosicaoInvalida(Exception):
    pass

class ListaCheiaException(Exception):
    pass

class ListaVaziaException(Exception):
    pass

class ListaSequencialArray:

    def __init__(self, capacidade = 5): #inicilia a lista vazia com o máximo de 5 elementoss
        self._capacidade = capacidade
        self._container = Array(self._capacidade)

    def _obtem_indice(self,index): #retorna o indice da lista
        if index <0:
            return self._capacidade + index
        return index
    
    @property
    def estaVazia(self) -> bool: #verifica se a lista está vazia, retorna True se estiver
        return not self._container
    
    @property
    def estaCheia(self) -> bool: # retorna True se a lista está cheia
        return self._container.cheio
    
    def __len__(self) -> int: #retorna  o tamanho da lista
        return self._container.tamanho
    
    def __geititem__(self,index): #retorna elemento na posição especificada pelo indice
        return self._container[self._obtem_indice(index)]
    
    def __contains__(self) -> bool:
        ...

    def __setitem__(self, index, valor): #Atribui o valor especificado ao elemento na posição especificada pelo índice
        index = self._obtem_indice(index) #obtem o indice do valor que será mudado
        if index >= len(self): #verificando se a posição é valida
            raise PosicaoInvalida("Posição inexistente!")
        self._container[index] = valor #se tudo estiver ok, o valor é alterado

    def _deslocar_a_direita(self,index,valor): #deslocar a lista a direita
        if self.estaCheia: #verifica a lista está cheia
            raise ListaCheiaException() #se estiver cheia, erro!
        
        index = self._obtem_indice(index) #obtem o indice
        if index >= len(self):#verificando se a posição é valida
            self._container[len(self)] = valor #o tamanho da lista vai receber o valor
        else:
            self._deslocar_a_direita(index)
            self[index]=valor

    def _deslocar_a_esquerda(self, index):
        for i in range(index, len(self) -1):
            self[i] = self[i+1]
        print(len(self))
        self._container[len(self)] = None
    
    def __delitem__ (self, index): #Remove o elemento na posição especificada pelo índice
        if self.estaVazia:
            raise ListaVaziaException()
        
        index = self._obtem_indice(index)
        if index >= len(self):
            raise PosicaoInvalida()
        
        self._deslocar_a_esquerda(index)

    
    def inserir_inicio(self,valor): #Insere o valor especificado no início da lista
        self.inserir(0, valor)

    def inserir_fim(self, valor): # Insere o valor especificado no final da lista.
        self.inserir(-1,valor)
        
    def remover_inicio(self): #Remove o primeiro elemento
        del self[0]

    def remover_fim(self): #Remove o último elementos
        del self[-1]

    def __repr__(self): #Retorna uma string que representa a lista
        result = ["["]

        for x in range(len(self)):
            result.append(str(self[x]))
            result.append(",")

        if not self.estaVazia:
            result.pop(-1)
        
        result.append("]")
        return "".join(result)
    
    def concatenar(self, segunda_lista): #Concatena a lista atual com outra lista.
        for x in range(len(segunda_lista)):
            self.inserir_fim(segunda_lista[x])

    def clonar(self) -> 'ListaSequencialArray': #Clona a lista atual.
        nova_lista = ListaSequencialArray()
        for x in range(len(self)):
            nova_lista.inserir_fim(self[x])
        return nova_lista
    
    def checar_duplicidade(self) -> bool: #Verifica se a lista possui elementos duplicados.
        for i in range(len(self)):
            for j in range(i+1, len(self)):
                if self[i] == self[j]:
                    return True
        return False
    
    def esvaziar(self): # Esvazia a lista.
        self._container = Array(capacidade=self._capacidade)

    def povoar(self): #Povoa a lista com números aleatórios.
        for x in range(self._capacidade):
            self.inserir(x, randint(0,10000))