class SeparateChainingHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash(key)
        chain = self.table[index]
        for item in chain:
            if item[0] == key:
                item[1] = value
                return
        chain.append((key, value))

    def search(self, key):
        index = self.hash(key)
        chain = self.table[index]
        for item in chain:
            if item[0] == key:
                return item[1]
        return None
