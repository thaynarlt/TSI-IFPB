class PilhaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class PilhaSequencial: #Utiliza uma LISTA
    def __init__(self):
        self.__dados = [] #iniciando a pilha
    
    def vazia(self): #verificar se pilha está vaziz
        return len(self.__dados) == 0
    
    def tamanho(self): #quantidade de elementos
        return len(self.__dados)
    
    def topo(self): #qual elemento está no topo da pilha
        if self.vazia():
            raise PilhaException('A pilha está vazia')
        return self.__dados[0]
    
    def inserir(self,dado): #inserindo na posição de indice ZERO
        self.__dados.insert(0,dado)
    
    def remover(self): #retirando no indice ZERO
        if self.vazia():
            raise PilhaException('A pilha está vazia')
        return self.__dados.pop(0)

    def __str__(self): #para imprimir a pilha
        return self.__dados.__str__()
    
    def imprimir(self):
        print(self.__str__())


if __name__ == "__main__":
    p = PilhaSequencial()

    for i in range(1,6):
        p.inserir(i * 10)

    print(p)
    try:
        p.remover()
    except PilhaException as pe:
        print(pe)

    print(p)

    
    