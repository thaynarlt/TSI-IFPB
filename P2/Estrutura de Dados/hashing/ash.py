
class Entry:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class Hash:

    def __init__(self, size=10):
        self._size = size
        self._table = [None for x in range(size)] # vetor que guarda os dados

    def _rehash(self, i):
        return (i+1) % self._size

    def _hash(self, key):
        return key % self._size

    def put(self, key, value):
        h = self._hash(key)
        if self._table[h] is None:
            self._table[h] = Entry(key, value)
        else:
            if self._table[h].key == key:
                self._table[h].value = value
            else:
                index = 2
                while index < self._size:
                    r = self._rehash(index)
                    if self._table[r] is None:
                        self._table[r] = Entry(key, value)
                    else:
                        if self._table[r].key == key:
                            self._table[r].value = value

                    index += 1
                    

    def get(self, key):
        entry = self._table[self._hash(key)]
        if entry:
            if entry.key == key:
                return entry.value
            else:
                index = 2
                while index < self._size:
                    r = self._rehash(index)
                    if self._table[r] is None:
                        return None
                    else:
                        if self._table[r].key == key:
                            return self._table[r].value
                    index += 1
        return None # key não existe


    def delete(self, key):
        entry = self._table[self._hash(key)]
        if entry:
            if entry.key == key:
                self._table[self._hash(key)] = None
            else:
                index = 2
                while index < self._size:
                    r = self._rehash(index)
                    if self._table[r] is None:
                        return None
                    else:
                        if self._table[r].key == key:
                            self._table[self._hash(key)] = None
                    index += 1
        return None # key não existe
        
    

if __name__ == "__main__":
    h = Hash()
    h.put(1, "Rodrigo")
    assert h._table[1].value == "Rodrigo"
    assert h.get(1) == "Rodrigo"
    h.put(2, "João")
    assert h.get(2) == "João"
    assert h._table[2].value == "João"
    h.put(1, "José")
    assert h.get(1) == "José"
    assert h._table[1].value == "José"
    h.put(11, "Maria")
    assert h._table[3].value == "Maria"
    assert h.get(11) == "Maria"
    assert h.get(1) == "José"