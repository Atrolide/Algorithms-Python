class HashTableDoubleHashing:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def hash2(self, key):
        return 1 + (hash(key) % (self.size - 1))

    def insert(self, key, value):
        index = self.hash(key)
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = value
        else:
            i = 1
            while True:
                index = (index + i * self.hash2(key)) % self.size
                if self.keys[index] is None:
                    self.keys[index] = key
                    self.values[index] = value
                    return
                elif self.keys[index] == key:
                    self.values[index] = value
                    return
                i += 1

    def search(self, key):
        index = self.hash(key)
        i = 1
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + i * self.hash2(key)) % self.size
            i += 1
        return None
