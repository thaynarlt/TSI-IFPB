class PilhaException(Exception):
    pass

class Node:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo: 'Node' | None = proximo


class PilhaEncadeada: #Não se usa LISTA
    def __init__(self):
        self.__tamanho: int = 0
        self.__topo: Node | None = None

    def estaVazia(self): #verifica se a pilha está vazia
        return self.__topo is None
    
    def tamanho(self): #retorna o tamanho da pilha
        return self.__tamanho

    def empilhar(self, elemento): #adiciona um elemento no topo da pilha
        self.__topo = Node(elemento, proximo=self.__topo)
        # if self.esta_vazia():
        #     self.__topo = Node(elemento)
        # else:
        #     novo_no = Node(elemento)
        #     novo_no.proximo = self.__topo
        #     self.__topo = novo_no
        self.__tamanho += 1        

    def desempilhar(self): #remove o elemento do topo da pilha
        if self.estaVazia():
            raise PilhaException()
        
        valor = self.__topo.valor
        self.__topo = self.__topo.proximo
        self.__tamanho -= 1
        return valor   
           
    def imprimir(self): #imprime os elementos da pilha
        no: Node = self.__topo
        print("[", end="")
        while no:
            print(f"{no.valor} ", end="")
            no = no.proximo
        print("]")

    def __str__(self):
        ...

    #retorna o valor do subtopo da pilha:   
    def subTopo(self): #método de instância da classe "PilhaEncadeada"
            if self.__tamanho < 2: #verificar se a pilha contém pelo menos dois elementos
                raise PilhaException("A pilha não tem subtopo.") # tamanho da pilha é armazenado na variável
                #Se a pilha tiver menos de dois elementos, há subtopo. E ai, exceção PilhaException é levantada


            # Se houver pelo menos dois elementos na pilha, retorne o valor do subtopo
            sub_topo = self.__topo.proximo.valor #obter o valor do subtopo da pilha, "self.__topo.proximo.valor" obtém o valor do subtopo.
            return sub_topo #retorna o valor do subtopo como resultado da função subTopo.
    