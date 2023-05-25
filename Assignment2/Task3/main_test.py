import numpy as np


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


class LinearProbingHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def hash(self, key):
        return key % self.capacity

    def insert(self, key, value):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.capacity
        self.keys[index] = key
        self.values[index] = value

    def search(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.capacity
        return None


class DoubleHashingHashTable:
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



def compare_search_insert_times(load_factors):
    import time
    import matplotlib.pyplot as plt

    sc_insertion_times = []
    sc_search_times = []
    lp_insertion_times = []
    lp_search_times = []
    dh_insertion_times = []
    dh_search_times = []

    for load_factor in load_factors:
        capacity = int(10000 * load_factor)

        separate_chaining_ht = SeparateChainingHashTable(capacity)
        linear_probing_ht = LinearProbingHashTable(capacity)
        double_hashing_ht = DoubleHashingHashTable(capacity)

        # Insertion
        start_time = time.time()
        for i in range(capacity):
            separate_chaining_ht.insert(i, i)
        insertion_time = time.time() - start_time
        sc_insertion_times.append(insertion_time)

        start_time = time.time()
        for i in range(capacity):
            linear_probing_ht.insert(i, i)
        insertion_time = time.time() - start_time
        lp_insertion_times.append(insertion_time)

        start_time = time.time()
        for i in range(capacity):
            double_hashing_ht.insert(i, i)
        insertion_time = time.time() - start_time
        dh_insertion_times.append(insertion_time)

        # Search
        start_time = time.time()
        for i in range(capacity):
            separate_chaining_ht.search(i)
        search_time = time.time() - start_time
        sc_search_times.append(search_time)

        start_time = time.time()
        for i in range(capacity):
            linear_probing_ht.search(i)
        search_time = time.time() - start_time
        lp_search_times.append(search_time)

        start_time = time.time()
        for i in range(capacity):
            double_hashing_ht.search(i)
        search_time = time.time() - start_time
        dh_search_times.append(search_time)

        print()

    # Plotting Insertion Times
    plt.plot(load_factors, sc_insertion_times, label="Separate Chaining Insertion")
    plt.plot(load_factors, lp_insertion_times, label="Linear Probing Insertion")
    plt.plot(load_factors, dh_insertion_times, label="Double Hashing Insertion")

    plt.xlabel("Load Factor")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Insertion Times vs. Load Factor")
    plt.legend()
    plt.show()

    # Plotting Search Times
    plt.plot(load_factors, sc_search_times, label="Separate Chaining Search")
    plt.plot(load_factors, lp_search_times, label="Linear Probing Search")
    plt.plot(load_factors, dh_search_times, label="Double Hashing Search")

    plt.xlabel("Load Factor")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Search Times vs. Load Factor")
    plt.legend()
    plt.show()


# Compare search/insert times for different load factors
# load_factors = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
load_factors = np.arange(0.1, 2.5 + 0.1, 0.1)
compare_search_insert_times(load_factors)