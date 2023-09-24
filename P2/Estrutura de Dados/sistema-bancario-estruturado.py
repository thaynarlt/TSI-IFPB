saldo = 0.0
depositos = []
saques = []
limite_diario = 500.0
saques_realizados = 0

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("O valor do depósito deve ser positivo.")

def sacar(valor):
    global saldo, saques_realizados
    if valor > 0:
        if saldo >= valor and saques_realizados < 3 and valor <= limite_diario:
            saldo -= valor
            saques.append(valor)
            saques_realizados += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif saques_realizados >= 3:
            print("Limite máximo de saques diários atingido.")
        elif valor > limite_diario:
            print("Limite de saque por operação excedido.")
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("O valor do saque deve ser positivo.")

def extrato():
    print("Extrato bancário:")
    print("Depósitos:")
    for deposito in depositos:
        print(f"  - Depósito de R$ {deposito:.2f}")
    print("Saques:")
    for saque in saques:
        print(f"  - Saque de R$ {saque:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")

# Exemplo de uso do sistema bancário
depositar(1000.0)
sacar(200.0)
sacar(300.0)
sacar(400.0)
sacar(100.0)
extrato()
