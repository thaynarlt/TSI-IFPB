from fila import FilaSequencialPython

def test():
    f = FilaSequencialPython()
    assert f.tamanho() == 0
    f.enfileirar("abc")
    f.tamanho() == 1
    v = f.desenfileirar()
    