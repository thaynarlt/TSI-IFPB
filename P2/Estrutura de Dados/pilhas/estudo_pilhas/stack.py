from node import Node

# Inserir na pilha
# Remover da pilha
# Observar o topo da pilha
class Stack:
    def __init__(self):
        self.top = None #top = topo da lista
        self._size = 0


    def push(self, elem): #Insere um elemento na pilha
        node = Node(elem)
        node.next = self.top #Move o novo elemento para o topo
        self.top = node #O nó que acabou de chegar vai para o topo da pilha
        self._size = self._size +1
        

    def pop(self, ): #Remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size -1
            return node.data
        raise IndexError("A pilha está vazia!")

    def peek(self):#Retorna o topo da pilha sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("A pilha está vazia!")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self): #Representação do objeto
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self): #Como se converte em uma string
        return self.__repr__() #Retorna String

#if __name__ == '__main__':
    # sequencial = []
    # sequencial.append(7)
    #lista = Stack()
    #lista.append(7)
    #lista.append(80)
    #lista.append(56)
    #lista.append(32)
    #lista.append(17)

pilha = Stack()
len(pilha)
pilha.push(3)
pilha.push(7)
pilha.push('python')
pilha.push(True)
pilha.push('Sucesso')
pilha.push(1.2)
print(pilha)

pilha.peek()
pilha.pop()
print(pilha)