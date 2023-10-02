import os

num1 = int(input())
num2 = int(input())

processId = os.fork()

if processId > 0:  # Código executado pelo processo pai
    espera = os.wait()

    with open('/tmp/pares.txt', 'r') as arquivo_resultado:
        resultados = arquivo_resultado.readlines()  # Lê todas as linhas do arquivo
        for resultado in resultados:
            print(resultado.strip())  # Remove a quebra de linha ao imprimir

else:
    with open('/tmp/pares.txt', 'w') as arquivo_resultado:  # Abre o arquivo no modo de escrita (cria ou sobrescreve)
        for _ in range(num1, num2+1):
            if _ % 2 == 0:
                arquivo_resultado.write(str(_) + '\n')  # Escreve cada número par em uma linha separada
