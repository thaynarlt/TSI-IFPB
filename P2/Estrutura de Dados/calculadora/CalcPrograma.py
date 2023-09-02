from Calculadora import Calculadora
import os

def interface(calculadora: object):
    print("+--------------+")
    print(f"|{calculadora.registrador:>14}|")
    print("+--------------+")
    print("(+) somar")
    print("(-) subtrair")
    print("(/) dividir")
    print("(*) multiplicar")
    print("(r) resetar")
    print("(d) desfazer")
    print("(off) desligar a calculadora")

def main():
    calc = Calculadora()
    while True:
        interface(calc)
        op = input(f"Informe a operação: ").lower()
        if op == "off":
            limpar_terminal()
            break
        if not validar_op(op):
            input('Opção inválida.\nPressione "ENTER" para continuar')
            limpar_terminal()
            continue
        if op == "r":
            calc.resetar()
            limpar_terminal()
            continue
        elif op == "d":
            calc.desfazer()
            limpar_terminal()
            continue
        limpar_terminal()
        interface(calc)
        valor = float(input(f"Informe o valor: "))
        calculo(calc, op, valor)
        limpar_terminal()


def validar_op(op: str) -> bool:
    return op in "+-*/rd"

def calculo(calc: object, op: str, valor: float):
    if op == "+":
        calc.somar(valor)
    elif op == "-":
        calc.subtrair(valor)
    elif op == "*":
        calc.multiplicar(valor)
    else:
        calc.dividir(valor)

def limpar_terminal():
    sistema = os.name
    if sistema == 'posix':
        os.system('clear')
    elif sistema == 'nt':
        os.system('cls')

if __name__ == "__main__":
    main()