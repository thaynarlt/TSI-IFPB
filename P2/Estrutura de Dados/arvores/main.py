from abb import Arvore

arvore = Arvore()
arvore.add(100)
arvore.remover(100)
assert arvore.raiz is None
arvore.add(100)
arvore.add(95)
arvore.add(70)
arvore.add(97)
arvore.add(96)
arvore.remover(95)
assert arvore.raiz.filho_esquerda.valor == 70
assert arvore.raiz.filho_esquerda.filho_direita.valor == 97