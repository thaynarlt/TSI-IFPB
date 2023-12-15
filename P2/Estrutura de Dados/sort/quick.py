def quickSort(array):
    _quick(array,0,len(array)-1)

def _quick(array,primeiro,ultimo):
    if primeiro<ultimo:
        splitpoint = particao(array,primeiro,ultimo)
        _quick(array,primeiro,splitpoint-1)
        _quick(array,splitpoint+1,ultimo)


def particao(array,primeiro,ultimo):
    pivo = array[primeiro]

    a = primeiro+1
    b = ultimo

    terminado = False
    while not terminado:

       while a <= b and array[a] <= pivo:
           a = a + 1

       while array[b] >= pivo and b >= a:
           b = b -1

       if b < a:
           terminado = True
       else:
           array[a], array[b] = array[b], array[a]

    array[primeiro], array[b] = array[b], array[primeiro]
    