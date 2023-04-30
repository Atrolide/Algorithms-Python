class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def search(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None