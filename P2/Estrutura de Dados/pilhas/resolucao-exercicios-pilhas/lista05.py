#1.
#lista 06 - Estrutura de Dados
class PilhaException(Exception):
    pass

class PilhaEncadeada:
    def __init__(self):
        self.__tamanho: int = 0
        self.__topo: Node | None = None

    def esta_vazia(self):
        return self.__topo is None

    def tamanho(self):
        return self.__tamanho

    def empilhar(self, elemento):
        self.__topo = Node(elemento, proximo=self.__topo)
        # if self.esta_vazia():
        #     self.__topo = Node(elemento)
        # else:
        #     novo_no = Node(elemento)
        #     novo_no.proximo = self.__topo
        #     self.__topo = novo_no
        self.__tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            raise PilhaException()
        
        valor = self.__topo.valor
        self.__topo = self.__topo.proximo
        self.__tamanho -= 1
        return valor

    def imprimir(self):
        no: Node = self.__topo
        print("[", end="")
        while no:
            print(f"{no.valor} ", end="")
            no = no.proximo
        print("]")
    
    def __str__(self): 
        ...
    
    def subTopo(self): #OK
        #retornar o sub-topo da pilha, sem desempilhar nenhum elemento:
        if self.__tamanho >= 2:
            subtopo = self.__topo.proximo
            return subtopo.valor
        raise PilhaException("A pilha não tem subtopo!")
    
    def desempilha_n(self, n:int): #desempilhe n elementos a partir do topo
        cont = 0
        if self.esta_vazia():
            raise PilhaException("A pilha está vazia")
        else:
            if n < self.__tamanho:
                while cont < n:
                    self.desempilhar()
                    cont+=1
                return True
            else:
                return False

    def esvazia(self):#Eliminar todos os elementos da pilha encadeada
        self.__topo = None
        self.__tamanho = 0

    
    def obtemBase(self): #retorna o conteúdo armazenado no nó da base da pilha, sem desempilhar nenhum elemento.
        if self.esta_vazia():
            raise PilhaException("A pilha está vazia")
        else:
            no: Node = self.__topo
            while no.proximo:
                no = no.proximo
            return no.valor
        
    def inverter(self): #Inverter a pilha
        pilha = PilhaEncadeada()
        while not self.esta_vazia():
            pilha.empilhar(self.desempilhar())

        self.__topo = pilha.__topo

    def concatenar(self, outra_pilha) -> 'PilhaEncadeada': #QUESTÃO DE PROVA
        #Unir as duas uma na outra // Pilha 2 venha pra baixo da Pilha 1
        pilha = PilhaEncadeada()
        while not self.esta_vazia():
            pilha.empilhar(self.desempilhar())

        while not outra_pilha.esta_vazia():
            pilha.empilhar(outra_pilha.desempilhar())

        pilha.inverter()
        return pilha



class Node:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo: 'Node' | None = proximo


variavel = PilhaEncadeada()
variavel.empilhar(15)
variavel.empilhar("teste")
variavel.empilhar("oi")
variavel.empilhar("tchau")
variavel.imprimir()
print(variavel.subTopo())

print(variavel.obtemBase())
variavel.imprimir()

