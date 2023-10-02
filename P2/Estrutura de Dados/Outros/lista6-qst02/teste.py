from Temporizador import Temporizador
from enum import Enum #Enumeração

class Estado(Enum):
    Vermelho = 1
    Amarelo = 2
    Verde = 3

class SemaforoTemporizado:
    #Definindo construtor
    def __init__(self, estadoInicial:Estado = Estado.Vermelho):
        #1: verde -> 20s| 2: laranja -> 5s| 3: vermelho -> 10s
        self.estadoAtual = estadoInicial
        self.timer = Temporizador()
        self.tempoDeTransicao = {Estado.Verde:20,\
                                Estado.Amarelo:5 ,\
                                Estado.Vermelho:10}

    def getEstadoAtual(self)->Estado:
        return self.estadoAtual

    def __str__(self):
        return f'''
        +--------+
        |  ( {"X" if self.estadoAtual == Estado.Vermelho else " "} )  |
        |  ( {"X" if self.estadoAtual == Estado.Amarelo else " "} )  |
        |  ( {"X" if self.estadoAtual == Estado.Verde else " "} )  |
        +--------+
        '''

    def setup(self,tempoVermelho:int, tempoAmarelo:int, tempoVerde:int):
        '''
        Método que permite ajustar o tempo dos estados do semáforo

        Argumentos
        -----------
        tempoVermelho(int): tempo em segundos em permanência no vermelho
        tempoAmarelo(int): tempo em segundos em permanência no amarelo
        tempoVerde(int): tempo em segundos em permanência no verde
        '''
        if tempoVermelho < 0 or tempoVermelho > 59:
            return
        elif tempoAmarelo < 1 or tempoAmarelo >59:
            return
        elif tempoVerde < 1 or tempoVerde>59:
            return
        self.tempoDeTransicao[Estado.Vermelho] = tempoVermelho
        self.tempoDeTransicao[Estado.Amarelo] = tempoAmarelo
        self.tempoDeTransicao[Estado.Verde] = tempoVerde
