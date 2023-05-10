class HashTableLinearProbing:
    # Constructor method, initializes size, keys and values lists.
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    # Hash function, returns the hash of a key using modulo operator.
    def hash(self, key):
        return hash(key) % self.size

    # Insert method, inserts a key-value pair into the hash table using linear probing.
    def insert(self, key, value):
        index = self.hash(key)
        while self.keys[index] is not None: # Loop until an empty index is found
            if self.keys[index] == key: # If the key is already present
                self.values[index] = value # Update the value
                return
            index = (index + 1) % self.size # Move to the next index using linear probing
        self.keys[index] = key # Insert the key
        self.values[index] = value # Insert the value

    # Search method, searches for a key in the hash table using linear probing.
    def search(self, key):
        index = self.hash(key)
        while self.keys[index] is not None: # Loop until an empty index is found
            if self.keys[index] == key: # If the key is found
                return self.values[index] # Return the corresponding value
            index = (index + 1) % self.size # Move to the next index using linear probing
        return None # Return None if the key is not found
