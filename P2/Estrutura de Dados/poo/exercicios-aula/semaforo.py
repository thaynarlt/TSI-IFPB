AMARELO = "amarelo"
VERMELHO = "vermelho"
VERDE = "verde"

class Temporizador:

	def __init__(self, ligado: bool):
		self.estah_ligado = ligado
		self.valor_atual: int | None = None


class Lampada:

	def __init__(self, cor: str, ligada: bool):
		self.cor = cor
		self.estah_ligada = ligada

	def acender(self):
		self.estah_ligada = True

	def apagar(self):
		self.estah_ligada = False


class Semaforo:
	contador = 0
	marca = "XingLing"

	def __init__(self):
		self.incrementa_contador()
		self.lampada_verde = Lampada(cor=VERDE, ligada=False)
		self.lampada_amarela = Lampada(cor=AMARELO, ligada=False)
		self.lampada_vermelha = Lampada(cor=VERMELHO, ligada=True)
		self.temporizador = Temporizador(ligado=False)

	@classmethod
	def incrementa_contador(cls):
		cls.contador += 1


sem = Semaforo()
print(sem.lampada_verde.estah_ligada)
sem.lampada_verde.acender()
print(sem.lampada_verde.estah_ligada)


print(Semaforo.marca)

