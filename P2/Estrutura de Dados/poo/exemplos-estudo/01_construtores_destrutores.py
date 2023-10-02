class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome=nome
        self.cor=cor
        self.acordado=acordado

    def __del__ (self):
        print("Removendo a instancia da classe.")
    
    def falar(self):
        print("AUAU")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)
    print(c.cor)
    print(c.acordado)

c = Cachorro("Chappie", "amarelo")
c.falar() #Aqui ele ta executando a classe

criar_cachorro() 

print('Olá mundo')

del c
print('Olá mundo')
print('Olá mundo')
print('Olá mundo')
