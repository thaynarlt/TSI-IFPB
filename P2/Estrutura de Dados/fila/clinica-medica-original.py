##Lista 08 // Questão 2 - Feito por Thayná (02/10/23)

# Atendimento por ordem de chegada
# Paciente deve fornecer: nome, CPF e plano de saúde (caso tenha)
# Após coleta de informações, paciente é adicionado ao sistema
# Assim que o cliente for adicionado, o sistema deverá fornecer a sua ordem de atendimento.


class Node: 
# A classe Node representa um nó de uma lista encadeada. 
# Um nó é uma unidade de dados que contém informações sobre um elemento da lista,
# bem como um ponteiro para o próximo nó da lista.

  def __init__(self, paciente, cpf, planosaude):
    #o nó contém informações sobre um elementos da fila
    self.paciente = paciente #nome do paciente
    self.cpf = cpf #cpf do paciente
    self.planosaude = planosaude #plano de saude do paciente
    self.proximo = None # próximo nó da lista

  def __repr__(self): #representação do nó como string
    return f'Node(valor={self.paciente})'


#------------------------------------------------------------------------------


class Paciente:

  def __init__(self, nome, cpf, planosaude):
    self.nome = nome
    self.cpf = cpf
    self.planosaude = planosaude


class FilaClinicaMedica:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enfileirar(self, paciente):
        novo_node = Node(paciente, paciente.cpf, paciente.planosaude)
        
        if self.inicio is None: # == if self.estah_vazia():
            self.inicio = novo_node
            self.fim = novo_node
        else:
            self.fim.proximo = novo_node
            self.fim = novo_node
        self.tamanho += 1
        return self.tamanho 

    def realizarChamada(self):
        if self.inicio is None:
            return None
        paciente = self.inicio
        self.inicio = self.inicio.proximo

        if self.inicio is None:
           self.fim = None

        self.tamanho -= 1
        return paciente
    
    def consultar_posicao(self, cpf):
        paciente = self.primeiro
        i = 1

        while paciente is not None:
            if paciente.cpf == cpf:
                return i

            paciente = paciente.proximo
            i += 1

        return None

    def listar_quantidade_atendidos(self):
        return self.tamanho

#-----------------------------------------------------

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
    clinica = FilaClinicaMedica()
    while True:
        escolha = menu()

        if escolha == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            plano_saude = input("Plano de saúde (opcional): ")
            paciente = Paciente(nome, cpf, plano_saude)
            posicao = clinica.enfileirar(paciente)
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