class Aluno: #Criação da classe "Aluno"
    def __init__(self, matricula: int, nome: str): #Atributos de instância matricula(int) e nome(string)
        if not isinstance(matricula, int) or len(str(matricula)) != 8: #Verfica se os dados estão corretos
            raise ValueError("A matrícula deve ser um número inteiro de 8 dígitos")
        
        self.__matricula = matricula #Criando as variáveis
        self.__nome = nome
        self.__notas = [] #Colocar as notas

    @property #permite que você acesse o nome do aluno como se fosse um atributo público
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def matricula(self):
        return self.__matricula

    def getMatriculaFormatada(self): #Formatando a matrícula para o formato desejado
        ano = str(self.__matricula // 10000)
        semestre = str((self.__matricula % 10000) // 1000)
        sequencial = str((self.__matricula % 10000) % 1000)

        if int(sequencial) <100 and int(sequencial)>=10:
            return f"{ano}.{semestre}.0{sequencial}"
        if int(sequencial) <10:
            return f"{ano}.{semestre}.00{sequencial}"
        else:
            return f"{ano}.{semestre}.{sequencial}"

    def media(self): #Aqui a média é feita
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas) #Media aritmética

    def adicionaNota(self, outraNota: int): #Adicionar as notas para as notas do aluno
        self.__notas.append(outraNota)


