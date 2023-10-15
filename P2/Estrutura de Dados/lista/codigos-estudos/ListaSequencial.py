


class ListaSequencial:
    
    def __init__(self): #inicia lista vazia
        self._container = []

    @property
    def estaVazia(self) -> bool: #retorna True se estiver vazia
        return not self._container

    @property
    def estaCheia(self) -> bool: #retorna True se estiver cheia
        return False
    
    def __len__(self) -> int: #retorna o tamanho da lista
        return len(self._container)
    
    def __getitem__(self, item): #retorna o elemento na posição especificada pelo indice
        return self._container[item]
    
    def __contains__(self,item) -> bool: #retorna True se o elemento especificado estiver na lista
        return item in self._container
    
    def __setitem__(self, index, valor): #Atribui o valor especificado ao elemento na posição especificada pelo índice
        self._container[index] = valor

    def inserir(self, index, valor): #insere um novo elemento na lista especificado pelo indice
        self._container.insert(index,valor)

    def __del__(self,index): #Remove o elemento na posição especificada pelo índice
        del self._container[index]

    def inserir_inicio(self,valor): #Insere o valor especificado no início da lista
        self._container.insert(0,valor)
    
    def inserir_fim(self,valor): #Insere o valor especificado no final da lista
        self._container.insert(len(self), valor)

    #ERRO
    def remover_inicio(self): #Remove o elemento do início da lista.
        del self[0]
    #ERRO
    def remover_fim(self): #Remove o elemento do final da lista.
        del self[len(self) -1]
    #ERRO
    def __repr__(self): #Retorna uma string que representa a lista.
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