# Реализация hashtable
import hashlib
import re


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[None] for _ in range(size)]

    def _hash(self, key):
        sha256_hash = hashlib.sha256(key.encode()).hexdigest()
        digits = re.findall('\d+', sha256_hash)
        return int(''.join(digits)) % self.size

    def get(self, key):
        slot = self._hash(key)
        for pair in self.table[slot]:
            if pair is not None and pair[0] == key:
                return pair[1]
        raise KeyError(f'Key {key} is not found')

    def add(self, key, value):
        slot = self._hash(key)
        for pair in self.table[slot]:
            if pair is not None and pair[0] == key:
                pair[1] = value
                return
        self.table[slot].append([key, value])

    def remove(self, key):
        slot = self._hash(key)
        for i in range(len(self.table[slot])):
            pair = self.table[slot][i]
            if pair is not None and pair[0] == key:
                del self.table[slot][i]
                return
        raise KeyError(f'Key {key} is not found')
