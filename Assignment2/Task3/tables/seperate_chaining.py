class HashTableSeparateChaining:
    # Constructor method, initializes size and table as a list of empty lists.
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function, returns the hash of a key using modulo operator.
    # hash function uses the built-in hash function to generate a hash value for the given key.
    def hash(self, key):
        return hash(key) % self.size

    # Insert method, inserts a key-value pair into the hash table using separate chaining.
    def insert(self, key, value):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key: # If the key is already present
                pair[1] = value # Update the value
                return
        self.table[index].append([key, value]) # Insert the key-value pair

    # Search method, searches for a key in the hash table using separate chaining.
    def search(self, key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key: # If the key is found
                return pair[1] # Return the corresponding value
        return None # Return None if the key is not found
