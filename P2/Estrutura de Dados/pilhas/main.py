from pilha import PilhaSequencial, PilhaException


def test_pilha_sequencial():
    p = PilhaSequencial()
    assert p.esta_vazia()
    p.empilhar(1)
    assert p.esta_vazia() == False
    assert p.tamanho() == 1
    valor = p.desempilhar()
    assert valor == 1
    assert p.tamanho() == 0
    p.empilhar(2)
    p.empilhar(3)
    p.empilhar(4)
    assert p.tamanho() == 3
    assert p.desempilhar() == 4
    assert p.desempilhar() == 3
    assert p.desempilhar() == 2
    assert p.esta_vazia()
    try:
        assert p.desempilhar() == 0
    except PilhaException:
        ...
    else:
        assert False, "Exceção não levantada"


if __name__ == "__main__":
    test_pilha_sequencial()