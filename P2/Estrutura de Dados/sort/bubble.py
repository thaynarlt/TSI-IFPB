from random import randint

def buble_sort(array: list) -> list:
    for i in range(len(array) - 1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


def selectionSort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min]


def insertion_sort(array: list):
    for i in range(1,len(array)):
        chave = array[i]
        j = i-1
        while j>=0 and chave < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = chave
    return array


# a = [randint(0, 100000) for x in range(10000)]

print(insertion_sort([100, 90, 4, 20, 5]))