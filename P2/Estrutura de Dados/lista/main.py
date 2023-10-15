from lista import ListaEncadeada

l = ListaEncadeada()
l.inserir(100, "a")
print(l)
l.inserir(1000, "z")
print(l)
l.inserir(1, "b")
print(l)
l.inserir(80, "zz")
print(l)
print(l._fim.valor)
print(l._inicio.valor)
l.inserir(3, "tres")
print(l)
l.inserir(0, "bug")
print(l)
l[1] = "posicao 1"
l[0] = "posicao 0"
print(l)
assert l[0] == "posicao 0"
assert "tres" in l