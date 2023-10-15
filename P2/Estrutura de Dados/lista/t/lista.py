from vetor import Vetor

class ListaSimples:

	def __init__(self):
		self._dados = []

	def estah_vazia(self):
		return self.tamanho == 0

	def estah_cheia(self):
		return False

	@property
	def tamanho(self):
		return len(self._dados)

	def obter_elemento(self, posicao):
		return self._dados[posicao]

	def modificar_elemento(self, posicao, valor):
		self._dados[posicao] = valor

	def inserir(self, posicao, valor):
		self._dados.insert(posicao, valor)

	def remover(self, posicao):
		del self._dados[posicao]

	def imprimir(self):
		print(self._dados)


class ErroIndice(Exception):
	pass

class ListaCheia(Exception):
	pass

class ListaVazia(Exception):
	pass


class ListaSequencial:

	def __init__(self, tamanho):
		self._tamanho = tamanho
		self._dados = Vetor(self._tamanho)

	def estah_vazia(self):
		return self.tamanho == 0

	def estah_cheia(self):
		return self._dados.tamanho == self._dados.quantidade

	@property
	def tamanho(self):
		return self._dados._quantidade

	def _validar_posicao(self, posicao):
		if not 0 <= posicao < self.tamanho:
			raise ErroIndice()

	def obter_elemento(self, posicao):
		self._validar_posicao(posicao)
		return self._dados[posicao]

	def modificar_elemento(self, posicao, valor):
		self._validar_posicao(posicao)
		self._dados[posicao] = valor

	def inserir(self, posicao, valor):
		if self.estah_cheia():
			raise ListaCheia()

		if posicao < 0:
			raise ErroIndice()
		elif posicao > self.tamanho:
			self._dados[self.tamanho] = valor
		else:
			self._deslocar_direita(posicao)
			self._dados[posicao] = valor

	def _deslocar_direita(self, posicao):
		for indice in range(self.tamanho, posicao, -1):
			self._dados[indice] = self._dados[indice - 1]

	def remover(self, posicao):
		if self.estah_vazia():
			raise ListaVazia()

		self._validar_posicao(posicao)
		self._deslocar_esquerda(posicao)

	def _deslocar_esquerda(self, posicao):
		for indice in range(posicao, self.tamanho - 1):
			self._dados[indice] = self._dados[indice + 1]

		self._dados[self.tamanho - 1] = None

	def imprimir(self):
		for indice in range(self.tamanho):
			print(self._dados[indice], end=" ")
		print()



class No:

	def __init__(self, dado, proximo=None):
		self.dado = dado
		self.proximo = proximo


class ListaEncadeada:

	def __init__(self):
		self._inicio: No = None
		self._tamanho: int = 0

	def estah_vazia(self) -> bool:
		return self._inicio is None

	def estah_cheia(self) -> bool:
		return False

	@property
	def tamanho(self):
		return self._tamanho

	def _obter_elemento(self, posicao):
		if posicao < 0:
			raise ErroIndice()

		posicao_atual = 0
		no = self._inicio
		while no is not None and posicao_atual < posicao:
			no = no.proximo
			posicao_atual += 1
		return no

	def obter_elemento(self, posicao):
		no = self._obter_elemento(posicao)
		return no.dado

	def modificar_elemento(self, posicao, valor):
		if not 0 <= posicao <= self.tamanho - 1:
			raise ErroIndice()
		
		no = self._obter_elemento(posicao)
		no.dado = valor

	def inserir(self, posicao, valor):
		novo_no = No(dado=valor)

		if posicao < 0:
			raise ErroIndice()
		elif posicao >= self.tamanho:
			# inserir na ultima posicao
			if self._inicio is None:
				self._inicio = novo_no
			else:
				ultimo = self._obter_elemento(self.tamanho - 1)
				ultimo.proximo = novo_no
		else:
			# inserir entre dois elementos
			antecessor = self._obter_elemento(posicao - 1)
			sucessor = antecessor.proximo
			antecessor.proximo = novo_no
			novo_no.proximo = sucessor

		self._tamanho += 1

	def remover(self, posicao):
		if posicao == 0:
			self._inicio = self._inicio.proximo
		elif posicao >= self.tamanho:
			raise ErroIndice()
		else:
			antecessor = self._obter_elemento(posicao - 1)
			antecessor.proximo = antecessor.proximo.proximo
		
		self._tamanho -= 1

	def imprimir(self):
		no = self._inicio
		while no is not None:
			print(no.dado, end=" ")
			no = no.proximo
		print()

	def __getitem__(self, posicao):
		return self.obter_elemento(posicao)

	def __setitem__(self, posicao, valor):
		self.modificar_elemento(posicao, valor)


def teste():
	l = ListaSequencial(10)
	assert l.estah_vazia() is True
	assert l.estah_cheia() is False
	l.inserir(0, "abc")
	assert l.tamanho == 1
	assert l.obter_elemento(0) == "abc"
	l.modificar_elemento(0, "zero")
	assert l.obter_elemento(0) == "zero"
	l.remover(0)
	assert l.tamanho == 0

if __name__ == "__main__":
	teste()