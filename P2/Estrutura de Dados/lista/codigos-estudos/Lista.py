class Lista:

    def __init__(self):
        ...

    @property
    def estah_vazia(self) -> bool:
        ...

    @property
    def estah_cheia(self) -> bool:
        ...

    def __len__(self) -> int: # tamanho
        ...

    def __getitem__(self, item): # obter
        ...

    def __contains__(self) -> bool:  # busca
        ...

    def __setitem__(self, item, valor): # modificar
        ...

    def inserir(self, valor):
        ...

    def __del__(self, index): # remover
        ...

    def inserir_inicio(self, valor):
        ...

    def inserir_fim(self, valor):
        ...

    def remover_inicio(self):
        ...

    def remover_fim(self):
        ...

    def __repr__(self):
        ...

    def concatenar(self):
        ...

    def clonar(self):
        ...

    def checar_duplicidade(self):
        ...

    def esvaziar(self):
        ...

    def povoar(self):
        ...
