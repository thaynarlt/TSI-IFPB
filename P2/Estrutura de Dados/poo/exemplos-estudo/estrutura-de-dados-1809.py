#Pilhas 18/09/23
#Inicio do conteúdo "Estrutura de Dados" + POO (Paradigma Orientado a Objetos)

#Exemplo PROGRAMAÇÃO ESTRUTURADA:
# Ventilador.py: TAD e Operacoes
# [ estaLigado, circulando]
ventilador = [False,False] # TAD

def liga():
    ventilador[0] = True
    print('Ligado')
def desliga():
    ventilador[0] = False
    print('Desligado')
def circular():
    ventilador[1] = True
    print('Circulando...')

# main.py

liga()
circular()
desliga()
ventilador[0]= 'Simmm' #Isso aqui é um exemplo de um ERRO
print(ventilador)

#-------------------------------------------------------------------------

#Exemplo PROGRAMAÇÃO ORIENTADA A OBJETOS

# Ventilador.py: TAD e Operacoes
class Ventilador:
    def __init__(self): # TAD
        self.__ligado = False
        self.__circulando = False
    def liga(self):
        self.__ligado = True
        print('Ligado')
    def desliga(self):
        self.__ligado = False
        print('Desligado')
    def circular(self):
        self.__circulando = True
        print('Circulando...')

# main.py
arno = Ventilador()
arno.liga()
arno.circular()
arno.desliga()
arno.__ligado = True