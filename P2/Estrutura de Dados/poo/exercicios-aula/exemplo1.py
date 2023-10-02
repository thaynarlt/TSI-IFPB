class Aluno:
	pass


rodrigo = Aluno()
rodrigo.nome = "Rodrigo"


def qq_funcao(self, idade):
	self.idade = idade


qq_funcao(rodrigo, 38)

print(rodrigo.idade)