import sys
import functools

def contagem_regressiva(n: int):
    if n > 0:
        contagem_regressiva(n-1)
        print(n)

def contagem_regressiva2(n: int):
    while n > 0:
        print(n)
        n = n - 1 


def fatorial(n: int) -> int:
    if n == 0:
        return 1
    return n * fatorial(n - 1)

# @functools.cache
def fibonacci(index: int) -> int:
    if index in (0, 1):
        return 1
    return fibonacci(index - 1) + fibonacci(index - 2)

def fibonacci2(n: int) -> int:
    if 0 <= n <= 1:
        return 1
    
    a = 1
    b = 1
    for x in range(2, n+1):
        c = a + b
        a = b
        b = c

    return c


cache = {0: 1, 1: 1}

def fibonacci3(index: int) -> int:
    if index in cache:
        return cache[index]
    else:
        value = fibonacci3(index - 1) + fibonacci3(index - 2)
        cache[index] = value
        return value
    

funcao = sys.argv[1]
n = int(sys.argv[2])
sys.setrecursionlimit(100000)

if funcao == 'recursiva':
    print(fibonacci(n))
elif funcao == 'iterativa':
    print(fibonacci2(n))
else:
    print(fibonacci3(n))