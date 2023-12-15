def mergeSort(arr):
    if len(arr) > 1:

        # Cria sub_array1 ← A[start..mid] e sub_array2 ← A[mid+1..end]
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        # Ordena as duas metades
        mergeSort(sub_array1)
        mergeSort(sub_array2)
     
        # Valores iniciais para os ponteiros que usamos para acompanhar onde estamos em cada array
        i = j = k = 0

        # Até chegarmos ao final de qualquer início ou final, escolhemos o maior entre
        # os elementos de início e fim e os colocamos na posição correta no array ordenado
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

        # Quando todos os elementos são percorridos em sub_array1 ou sub_array2,
        # pegamos os elementos restantes e os colocamos no array ordenado
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
