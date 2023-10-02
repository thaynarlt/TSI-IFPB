class PilhaException(Exception):
    """Classe de exceção lançada quando uma violação de acesso aos elementos
       da pilha é identificada.
    """
    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)


        
class Pilha:
    """A classe Pilha.py implementa a estrutura de dados "Pilha".
       A classe permite que qualquer tipo de dado seja armazenada na pilha.

     Attributes:
        dado (list): uma estrutura de armazenamento dinâmica dos elementos da
             pilha
    """
    def __init__(self):
        """ Construtor padrão da classe Pilha sem argumentos. Ao instanciar
            um objeto do tipo Pilha, esta iniciará vazia. 
        """
        self.__dado = []



    def estaVazia(self):
        """ Método que verifica se a pilha está vazia ou não

        Returns:
            boolean: True se a pilha estiver vazia, False caso contrário

        Examples:
            p = Pilha()
            ...   # considere que temos internamente na pilha [10,20,30,40]<- topo
            if(p.estaVazia()): #
               # instrucoes
        """
        return True if len(self.__dado)==0 else False

    def tamanho(self):
        """ Método que consulta a quantidade de elementos existentes na pilha

        Returns:
            int: um número inteiro que determina o número de elementos existentes na pilha

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<- p
            print (p.tamanho()) # exibe 4
        """        
        return len(self.__dado)


    def elemento(self, posicao):
        """ Método que recupera o valor armazenado em um determinado elemento da pilha

        Args:
            posicao (int): um número correpondente à ordem do elemento existente,
                na direção da base até o topo
        
        Returns:
            int: o valor armazenado na ordem indicada por posição.

        Raises:
            PilhaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a um elemento que excede a
                      quantidade de elementos da lista.                      
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<-topo
            posicao = 5
            print (p.elemento(3)) # exibe 30
        """
        try:
            assert posicao > 0
            return self.__dado[posicao-1]
        except IndexError:
            raise PilhaException(f'Posicao {posicao} invalida para a Pilha')
        except TypeError:
            raise PilhaException(f'O tipo de dado para posicao não é um número inteiro')
        except AssertionError:
            raise PilhaException(f'A posicao deve ser um número maior que zero')
        except:
            raise

    
    def busca(self, valor):
        """ Método que recupera a posicao ordenada, dentro da pilha, em que se
            encontra um valor passado como argumento. No caso de haver mais de uma
            ocorrência do valor, a primeira ocorrência será retornada

        Args:
            valor: um item de dado que deseja procurar na pilha
        
        Returns:
            int: um número inteiro representando a posição, na pilha, em que foi
                 encontrado "valor".

        Raises:
            PilhaException: Exceção lançada quando o argumento "valor"
                  não está presente na pilha.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]<-topo
            print (p.elemento(40)) # exibe 4
        """
        try:
            return self.__dado.index(valor) + 1
        except ValueError:
            raise PilhaException(f'O valor {valor} não está armazenado na pilha')
        except:
            raise

    def topo(self):
        """ Método que devolve o elemento localizado no topo, sem desempilhá-lo
    
        Returns:
            qualquer tipo de dado: o conteúdo referente ao elemento do topo

        Raises:
            PilhaException: Exceção lançada quando se tenta consultar o topo de uma
                   uma pilha vazia
                    
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = p.topo()
            print(dado) # exibe 40
        """
        try:
            return self.__dado[-1]
        except IndexError:
            raise PilhaException(f'Pilha Vazia. Não há elemento no topo')
        except:
            raise


    def empilha(self, valor ):
        """ Método que adiciona um novo elemento ao topo da pilha

        Args:
            valor(qualquer tipo de dado): o conteúdo que deseja armazenar
                  na lista.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            p.empilha(50)
            print(p)  # exibe [10,20,30,40,50]
        """
        self.__dado.append(valor)


    def desempilha(self):
        """ Método que remove um elemento do topo da pilha e devolve o conteudo
            existente removido.
    
        Returns:
            qualquer tipo de dado: o conteúdo referente ao elemento removido

        Raises:
            PilhaException: Exceção lançada quando se tenta remover algo de uma pilha vazia
                    
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = p.desemplha()
            print(p) # exibe [10,20,30]
            print(dado) # exibe 40
        """
        try:
            return self.__dado.pop()
        except IndexError:
            raise PilhaException(f'Pilha Vazia. Não é possível efetuar a remoção')
        except:
            raise


    def imprimir(self):
        """ Método que exibe a sequência ordenada dos elementos da pilha

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<-topo
            p.imprimir()) # exibe Lista: [10,20,30,40] <- topo
        """  
        print(self.__dado.__str__() + '<-topo')


        
    def __str__(self):
        return self.__dado.__str__()



if __name__ == '__main__':
       

    def imprimeInvertido(str):
        p = Pilha()
        for s in str:
            if (s==' '):
                try:
                    while(True):
                        print(p.desempilha(),end='')
                except:
                    print(' ',end='')
            else:
                p.empilha(s)
        if not p.estaVazia():
            try:
                while(True):
                    print(p.desempilha(),end='')
            except:
                pass
        
    
    p = Pilha()
    try:
        for i in range(1,10):
            p.empilha(i*10)
        print(p.desempilha())
        p.empilha('alex')
        #p.imprimir()
        print(p)
  
        #print(p.elemento(-8))
        #print(p.elemento(10))
        #print(p.elemento('a'))

        print(p.elemento(3))
        print(p.busca(80))
        #print(p.busca('joao'))
        p.imprimir()

        '''
        #lst.busca(40)
        print('Inserindo o valor 50 na 2a posicao')
        lst.inserir(2,50)
        print('Valor inserido com sucesso!')
        print(lst)
        valor = lst.remover(4)
        print('valor:',valor)
        print(lst)
        #valor = lst.remover(10)
        lst.imprimir()
        '''

        imprimeInvertido('Estrutura de Dados')
    except PilhaException as pe:
        print(pe)
    except Exception as e:
        print('Nossos engenheiros vao analisar esse problema')
    except:
        print('FIM')

     

    
        


        
