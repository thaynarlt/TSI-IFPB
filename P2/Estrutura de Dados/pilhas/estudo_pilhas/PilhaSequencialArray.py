from array_ifpb import Array

class PilhaException(Exception):
    pass

class PilhaSequencialArray:
    def __init__(self):
        self.__topo = 0
        self.__dados = Array(3) #quantidade máxima de elementos na pilha

    def estaVazia(self): #verifica se está vazia com base no array_ifpb
        return self.__dados.vazio
    
    def tamanho(self): #verifica o tamanho com base no array_ifpb
        return self.__dados.tamanho
    
    def empilhar(self, elemento):
        if self.__dados.cheio: #Se a pilha estiver cheia:
            # Para adicionar um novo elemento à pilha, é necessário criar
            # um novo array com o dobro da capacidade do array atual.
            novo = Array(self.__dados.capacidade * 2) #novo array é atribuído à variável 'novo'
            novo.copiar_de(self.__dados) #copiar os elementos do array atual para o novo array
            self.__dados = novo

        self.__dados[self.__topo] = elemento #atribuir o novo array ao atributo self.__dados da pilha
        self.__topo += 1
        #o índice self.__topo é incrementado para indicar que um novo elemento foi adicionado à pilha

    def desempilhar(self): #remover o elemento no topo da pilha
        if self.esta_vazia(): #se a pilha estiver vazia, raise o erro PilhaException
            raise PilhaException()

        # Remove o elemento no topo da pilha:
        posicao = self.__topo - 1 #acessa a posição do elemento no array
        valor = self.__dados[posicao] #atribui o valor do elemento à variável valor
        del self.__dados[posicao] #função remove o elemento do array usando o método del

        # Verifica se a pilha está abaixo da metade de sua capacidade:
        porcentagem_uso = (self.__dados.tamanho // self.__dados.capacidade) * 100
        if porcentagem_uso < 50: #verifica se a pilha está abaixo da metade de sua capacidade
            novo = Array(self.__dados.capacidade // 2) #reduz a capacidade do array pela metade
            # é feito para evitar o desperdício de memória.
            novo.copiar_de(self.__dados)
            self.__dados = novo

        self.__topo -= 1 #Decrementa o índice self.__topo
        #para indicar que um elemento foi removido da pilha
        return valor





if __name__ == "__main__":
    p = PilhaSequencialArray()

    p.empilhar(1)
    p.empilhar(2)
    p.empilhar(3)
    print(p)
    p.empilhar(4)


