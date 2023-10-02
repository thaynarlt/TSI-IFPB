
class PessoaIFPB:

    def __init__(self):
        self.cpf = "000.000.00-89"
        self.__matricula = "123"


class Professor(PessoaIFPB):

    def __init__(self):
        self.matricula = "1234"



p = Professor()