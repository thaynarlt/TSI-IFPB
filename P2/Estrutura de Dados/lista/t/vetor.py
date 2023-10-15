class VetorPosicaoError(Exception):
	pass


class Vetor:

	def __init__(self, tamanho):
		self._tamanho = tamanho
		self._quantidade = 0
		self._dados = [None] * tamanho

	def _validar_posicao(self, posicao):
		if not 0 <= posicao < self._tamanho:
			raise VetorPosicaoError("posição inválida")

	def get(self, posicao):
		self._validar_posicao(posicao)
		return self._dados[posicao]

	def set(self, posicao, valor):
		self._validar_posicao(posicao)

		if self._dados[posicao] is None:
			self._quantidade += 1
		elif valor is None:
			self._quantidade -= 1

		self._dados[posicao] = valor

	@property
	def tamanho(self):
		return self._tamanho

	@property
	def quantidade(self):
		return self._quantidade

	def __getitem__(self, posicao):
		return self.get(posicao)

	def __setitem__(self, posicao, valor):
		return self.set(posicao, valor)

	def __len__(self):
		return self.tamanho

	def __repr__(self):
		return repr(self._dados)

	@classmethod
	def novo_vetor(cls, novo_tamanho, vetor_antigo):
		v2 = cls(novo_tamanho)
		for indice in range(vetor_antigo.quantidade):
			v2[indice] = vetor_antigo[indice]
		return v2



def teste():
	v = Vetor(tamanho=10)
	assert len(v) == 10
	assert v[1] is None
	assert v.quantidade == 0
	v[1] = "abc"
	assert v.quantidade == 1
	assert v[1] == "abc"
	v[1] = None
	assert v.quantidade == 0

	assert v[1] is None
	v[2] = "teste"
	assert v[2] == "teste"
	assert len(v) == 10


if __name__ == "__main__":
	teste()
