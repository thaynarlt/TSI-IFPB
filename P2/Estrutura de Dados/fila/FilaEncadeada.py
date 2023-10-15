class FilaVaziaException(Exception):
    pass

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
    
    def enfileirar(self, valor) -> None:
        elemento = Node(valor) #cria um novo nó com o valor
        if self.estaVazia(): #verifica se está vazia
            self.__inicio = elemento #se estiver, o novo nó será o inicio e o fim da fila
        else: #se não
            self.__fim.proximo = elemento #o novo nó será anexado ao fim da fila
            self.__tamanho +=1 #atualiza o tamanho da fila

    def desenfileirar(self):
        if self.estaVazia(): # se a fila estiver vazia
            raise FilaVaziaException() #vai levantar o erro
        valor = self.__inicio.valor #recupera o valor do primeiro elemento da fila
        self.__inicio = self.__inicio.proximo #atualiza o atributo __inicio para apontar para o próximo elemento da fila.
        self.__tamanho -=1 #diminui o tamanho da fila
        return valor

    def busca(self,valor) -> bool:
        no = self.__inicio #iteração no primeiro nó
        while no !=None:
            # cada iteração, a função compara o valor do nó atual 
            # com o valor passado como parâmetro.
            if no.valor == valor:
                return True #Se os valores forem iguais, a função retorna True.
            no = no.proximo #e os valores forem diferentes, a função avança para o próximo nó.
            return False #caso não tenha, retorna falso
    
    def __contains__(self,valor): #usada para verificar se um valor está presente
        return self.busca(valor)
    #chama a função busca para verificar se o valor está presente na fila

    def __str__(self): #impressão da fila
        result = ["["]

        no = self.__inicio
        while no != None:
            result.append(str(no.valor))
            result.append(",")
            no = no.proximo

        if not self.estaVazia():
            result.pop(-1)
        result.append("]")
        return "".join(result)