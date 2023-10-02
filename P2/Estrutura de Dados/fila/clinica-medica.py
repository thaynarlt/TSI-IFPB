#Lista 08 // Questão 2
class Paciente:
    def __init__(self, nome, cpf, plano_saude): #contrutor __init__ recebe dados dos pacientes como parâmetros
        self.nome = nome
        self.cpf = cpf
        self.plano_saude = plano_saude


class Fila: #Fila da Clínica Médica
    def __init__(self): #Construtor inicia a fila vazia
        self.pacientes = []

    def incluir(self, paciente): #Serve para adicionar paciente a fila
        self.pacientes.append(paciente) #Paciente adicionado
        return len(self.pacientes) #Tamanho da fila é retornado

    def realizar_chamada(self): #Chama o próximo paciente da fila
        if len(self.pacientes) == 0: #--Se a fila estover vazia retorna None
            return None

        paciente = self.pacientes.pop(0) #Paciente do início da fila é removido e retornado 
        return paciente

    def consultar_posicao(self, cpf): #Retorna a posição atual de um paciente
        for i, paciente in enumerate(self.pacientes):
            if paciente.cpf == cpf: #Se o paciente for encontrado por seu cpf
                return i + 1 #Sua posição na fila é retornada
        return None

    def listar_quantidade_atendidos(self): #Quantidade de pacientes atendidos
        return len(self.pacientes) #Quantidade de pacientes na fila


def menu(): #Menu do programa
    print("Clinica Medica - Atendimento")
    print("=============")
    print("1. Incluir paciente")
    print("2. Realizar chamada")
    print("3. Consultar a posição atual")
    print("4. Listar a quantidade de pacientes atendidos")
    print("5. Sair")

    escolha = input("Digite sua escolha: ")
    return escolha


def main(): #Ponto de entrada do programa
    clinica = Fila()
    while True:
        escolha = menu()
        #Escolhas do menu
        if escolha == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            plano_saude = input("Plano de saúde (opcional): ")
            paciente = Paciente(nome, cpf, plano_saude)
            posicao = clinica.incluir(paciente)
            print("Paciente incluído com sucesso! Posição: {}".format(posicao))

        elif escolha == "2":
            paciente = clinica.realizar_chamada()
            if paciente is None:
                print("Não há pacientes na fila.")
            else:
                print("Paciente chamado: {}".format(paciente.nome))

        elif escolha == "3":
            cpf = input("Digite o CPF do paciente: ")
            posicao = clinica.consultar_posicao(cpf)
            if posicao is None:
                print("Paciente não encontrado.")
            else:
                print("Posição atual do paciente: {}".format(posicao))

        elif escolha == "4":
            quantidade = clinica.listar_quantidade_atendidos()
            print("Quantidade de pacientes atendidos: {}".format(quantidade))

        elif escolha == "5":
            print("Saindo...")
            break


if __name__ == "__main__":
    main()