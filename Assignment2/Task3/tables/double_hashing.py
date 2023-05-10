class HashTableDoubleHashing:
    # Constructor method, initializes size, keys and values lists.
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    # Hash function, returns the hash of a key using modulo operator.
    def hash(self, key):
        return hash(key) % self.size

    # Second hash function used for probing, returns 1 plus the hash of a key modulo size - 1.
    def hash2(self, key):
        return 1 + (hash(key) % (self.size - 1))

    # Insert method, inserts a key-value pair into the hash table using double hashing.
    def insert(self, key, value):
        index = self.hash(key)
        if self.keys[index] is None: # If the index is empty
            self.keys[index] = key # Insert key
            self.values[index] = value # Insert value
        else: # If the index is not empty
            i = 1
            while True: # Loop until an empty index is found
                index = (index + i * self.hash2(key)) % self.size # Double hash
                if self.keys[index] is None: # If an empty index is found
                    self.keys[index] = key # Insert key
                    self.values[index] = value # Insert value
                    return
                elif self.keys[index] == key: # If key is already present
                    self.values[index] = value # Update value
                    return
                i += 1

    # Search method, searches for a key in the hash table using double hashing.
    def search(self, key):
        index = self.hash(key)
        i = 1
        while self.keys[index] is not None: # Loop until an empty index is found
            if self.keys[index] == key: # If the key is found
                return self.values[index] # Return the corresponding value
            index = (index + i * self.hash2(key)) % self.size # Double hash
            i += 1
        return None # Return None if the key is not found
