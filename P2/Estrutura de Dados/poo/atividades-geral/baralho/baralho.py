import random
from enum import Enum

class BaralhoExeception(Exception):
    pass

class NumJogadoresInvalido(BaralhoExeception):
    pass


class Naipe(Enum):
    OUROS = 1
    PAUS = 2
    COPAS = 3
    ESPADAS = 4

class Carta:
    AS = 1
    VALETE = 11
    RAINHA = 12
    REI = 13
    
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor
        self.nome = self._get_nome()

    def _get_nome(self):
        match self.valor:
            case 1:
                return "Ás"
            case x if 2 <= x <= 10:
                return str(self.valor)
            case 11:
                return "Valete"
            case 12:
                return "Rainha"
            case 13:
                return "Rei"
            case _:
                raise ValueError("valor inválido")
            
    def __str__(self):
        return f'{self.nome} de {self.naipe.name.title()}'
    
    def __repr__(self):
        return f'Carta({self})'
    
    def __lt__(self, outra_carta: 'Carta') -> bool:
        return self.valor < outra_carta.valor
    
    def __eq__(self, outra_carta: 'Carta') -> bool:
        return self.valor == outra_carta.valor

class Baralho:
    
    def __init__(self):
        self._criar_cartas()
        self._embaralhar()
    
    def __len__(self):
        return len(self.cartas)
    
    def _criar_cartas(self):
        self.cartas = []
        for naipe in Naipe:
            for valor in range(1, 14):
                self.cartas.append(
                    Carta(valor=valor, naipe=naipe)
                )
    
    def _embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self, *jogadores):
        if not 1 <= len(jogadores) <= 4:
            raise NumJogadoresInvalido(f'Valor={len(jogadores)}')

        quantidade = len(self) // len(jogadores)
        for i in range(len(jogadores)):
            jogadores[i].adicionar_cartas( self.cartas[i * quantidade: (i+1)*quantidade] )




class Jogador:
    
    def __init__(self, nome):
        self.nome = nome
        self.deck = []

    def __repr__(self):
        return f'Jogador({self.nome})'
    
    def adicionar_cartas(self, cartas):
        self.deck.extend(cartas)

    def adicionar_carta(self, carta: Carta):
        self.deck.append(carta)

    def pegar_Carta(self) -> Carta:
        return self.deck.pop(0)    


class Jogo:
    def __init__(self, nome_jogador_1 str, nome_jogador_2: str):
        self.baralho = Baralho()
        self.nome_jogador_1
        





b = Baralho()
j1 = Jogador("Rodrigo")
j2 = Jogador("Pinheiro")
j3 = Jogador("Marques")
j4 = Jogador('Araujo')
j5 = Jogador('Mickey')
b.distribuir(j1, j2, j3, j4)

try:
    b.distribuir(j1,j2,j3,j4,j5)
    print('1,2,3')
except BaralhoExeception as error:
    print(f'Quantidade de jogadores inválida!{error.args[0]}')
except ZeroDivisionError as error:
    print('Deu ruim!')
finally:
    print('4,5,6')