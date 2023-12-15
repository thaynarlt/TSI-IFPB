def buscaBinaria(array, chave):
    inicio = 0
    fim = len(array)-1
    # Enquanto houver distância entre inicio e fim
    while (inicio <= fim ):
        meio = (inicio + fim)//2
        if ( chave < array[meio] ):
            fim = meio - 1 # Ajusta a pos. final
        elif ( chave > array[meio] ):
            inicio = meio + 1 # Ajusta a pos. inicial
        else:
            return meio # elemento foi encontrado!

    # Se finalizar o laço, percorreu todo o array e
    # não encontrou
    return -1