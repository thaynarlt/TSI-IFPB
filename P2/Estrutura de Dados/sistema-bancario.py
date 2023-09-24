class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.limite_diario = 500.0
        self.saques_realizados = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor and self.saques_realizados < 3 and valor <= self.limite_diario:
                self.saldo -= valor
                self.saques.append(valor)
                self.saques_realizados += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            elif self.saques_realizados >= 3:
                print("Limite máximo de saques diários atingido.")
            elif valor > self.limite_diario:
                print("Limite de saque por operação excedido.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def extrato(self):
        print("Extrato bancário:")
        print("Depósitos:")
        for deposito in self.depositos:
            print(f"  - Depósito de R$ {deposito:.2f}")
        print("Saques:")
        for saque in self.saques:
            print(f"  - Saque de R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


# Exemplo de uso do sistema bancário
sistema = SistemaBancario()

sistema.depositar(1000.0)
sistema.sacar(200.0)
sistema.sacar(300.0)
sistema.sacar(400.0)
sistema.sacar(100.0)
sistema.extrato()
