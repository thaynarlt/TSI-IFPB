#Lista 08 // Questão 2
class Paciente:
    def __init__(self, nome, cpf, plano_saude):
        self.nome = nome
        self.cpf = cpf
        self.plano_saude = plano_saude


class Fila:
    def __init__(self):
        self.pacientes = []

    def incluir(self, paciente):
        self.pacientes.append(paciente)
        return len(self.pacientes)

    def realizar_chamada(self):
        if len(self.pacientes) == 0:
            return None

        paciente = self.pacientes.pop(0)
        return paciente

    def consultar_posicao(self, cpf):
        for i, paciente in enumerate(self.pacientes):
            if paciente.cpf == cpf:
                return i + 1
        return None

    def listar_quantidade_atendidos(self):
        return len(self.pacientes)


def menu():
    print("Clinica Medica - Atendimento")
    print("=============")
    print("1. Incluir paciente")
    print("2. Realizar chamada")
    print("3. Consultar a posição atual")
    print("4. Listar a quantidade de pacientes atendidos")
    print("5. Sair")

    escolha = input("Digite sua escolha: ")
    return escolha


def main():
    clinica = Fila()
    while True:
        escolha = menu()

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