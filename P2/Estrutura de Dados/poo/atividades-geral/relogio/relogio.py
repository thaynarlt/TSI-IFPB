
class Relogio:

	def __init__(self, horas: int, minutos: int, segundos: int):
		self.horas = self.set_hora(horas)
		self.minutos = self.set_minuto(minutos)
		self.segundos = self.set_segundo(segundos)

	def get_horas(self):
		return self.horas

	def get_minutos(self):
		return self.minutos

	def get_segundos(self):
		return self.segundos

	def get_hora_como_string(self) -> str:
		return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

	def imprimir(self):
		print(self.get_hora_como_string())

	def set_hora(self, valor: int):
		if 0 <= valor <= 23:
			self.horas = valor
		else:
			self.horas = 0

	def set_minuto(self, valor: int):
		if 0 <= valor <= 59:
			self.minutos = valor
		else:
			self.minutos = 0

	def set_segundo(self, valor: int):
		if 0 <= valor <= 59:
			self.segundos = valor
		else:
			self.segundos = 0

	def add_hora(self, valor: int):
		self.horas = (self.horas + valor) % 24

	def add_minuto(self, valor: int):
		horas, self.minutos = divmod(self.minutos + valor, 60)
		self.add_hora(horas)

	def add_segundo(self, valor: int):
		minutos, self.segundos = divmod(self.segundos + valor, 60)
		self.add_minuto(minutos)





class Relogio:

	def __init__(self, segundos=0):
		self.segundos: int = segundos

	def get_horas(self):
		quociente = self.segundos // 3600
		if quociente < 24:
			return quociente
		return quociente % 24

	def get_minutos(self):
		quociente = self.segundos // 60
		if quociente < 60:
			return quociente
		return quociente % 60

	def get_segundos(self):
		return self.segundos % 60

	def get_hora_como_string(self) -> str:
		return f'{self.get_horas():02d}:{self.get_minutos():02d}:{self.get_segundos():02d}'

	def imprimir(self):
		print(self.get_hora_como_string())

	def set_hora(self, valor: int):
		diferenca = valor - self.get_horas()
		self.add_hora(diferenca)

	def set_minuto(self, valor: int):
		diferenca = valor - self.get_minutos()
		self.add_minuto(diferenca)

	def set_segundo(self, valor: int):
		diferenca = valor - self.get_segundos()
		self.add_segundo(diferenca)


	def add_hora(self, valor: int):
		self.segundos += (valor * 60 * 60)

	def add_minuto(self, valor: int):
		self.segundos += (valor * 60)

	def add_segundo(self, valor: int):
		self.segundos += valor

	def __str__(self):
		return f'Relogio({self.get_hora_como_string()})'

	def __add__(self, outro_relogio):
		return Relogio(self.segundos + outro_relogio.segundos)









