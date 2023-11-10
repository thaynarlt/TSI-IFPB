
def soma_lista(a_lista) -> int:
    if len(a_lista) == 0:
        return 0
    
    # cabeca, *resto = a_lista
    # return cabeca + soma_lista(resto)

    cabeca = a_lista[0]
    resto = a_lista[1:]
    return cabeca + soma_lista(resto)


assert soma_lista([1, 2, 3]) == 6
assert soma_lista([1, 2]) == 3


def recursive_length(string) -> int:
    if string == "":
        return 0
    return 1 + recursive_length(string[1:])

assert recursive_length("") == 0
assert recursive_length("a") == 1
assert recursive_length("ab") == 2

def invert_string(string) -> str:
    if string == "":
        return ""
    return invert_string(string[1:]) + string[0]

assert invert_string("abc") == "cba"