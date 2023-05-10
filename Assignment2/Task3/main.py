import time
import matplotlib.pyplot as plt
from tables import *
import random

# n is the number of key-value pairs that will be inserted into each hash table
# load_factor is the ratio of the number of key-value pairs to the size of the hash table.
# It is used to determine the size of the hash table for each implementation.
import time
import matplotlib.pyplot as plt


def test(load_factor, n):
    keys = [str(i) for i in range(n)]
    values = [i for i in range(n)]

    sep_chain_ht = HashTableSeparateChaining(int(n / load_factor))
    linear_probe_ht = HashTableLinearProbing(int(n / load_factor))
    double_hash_ht = HashTableDoubleHashing(int(n / load_factor))

    # Insert keys and values into hash tables
    for i in range(5):
        sep_chain_ht.insert(keys[i], values[i])
        linear_probe_ht.insert(keys[i], values[i])
        double_hash_ht.insert(keys[i], values[i])

    # Time the search operation for each load factor
    timer = time.perf_counter
    times = []
    for i in range(5):
        start_time = timer()
        for key in keys:
            sep_chain_ht.search(key)
        end_time = timer()
        times.append(end_time - start_time)
    sep_chain_avg_time = sum(times) / len(times)

    times = []
    for i in range(5):
        start_time = timer()
        for key in keys:
            linear_probe_ht.search(key)
        end_time = timer()
        times.append(end_time - start_time)
    linear_probe_avg_time = sum(times) / len(times)

    times = []
    for i in range(5):
        start_time = timer()
        for key in keys:
            double_hash_ht.search(key)
        end_time = timer()
        times.append(end_time - start_time)
    double_hash_avg_time = sum(times) / len(times)

    # Create a chart to compare search times at different load factors
    x = [i/10 for i in range(1, 11)]
    sep_chain_y = [0] * 10
    linear_probe_y = [0] * 10
    double_hash_y = [0] * 10

    sep_chain_ht = HashTableSeparateChaining(int(n / load_factor))
    linear_probe_ht = HashTableLinearProbing(int(n / load_factor))
    double_hash_ht = HashTableDoubleHashing(int(n / load_factor))

    for j in range(n):
        sep_chain_ht.insert(keys[j], values[j])
        linear_probe_ht.insert(keys[j], values[j])
        double_hash_ht.insert(keys[j], values[j])

        times = []
        for j in range(5):
            start_time = timer()
            for key in keys:
                sep_chain_ht.search(key)
            end_time = timer()
            times.append(end_time - start_time)
        sep_chain_y[i] = sum(times) / len(times)

        times = []
        for j in range(5):
            start_time = timer()
            for key in keys:
                linear_probe_ht.search(key)
            end_time = timer()
            times.append(end_time - start_time)
        # linear_probe_avg_time = sum(times) / len(times)
        linear_probe_y[i] = sum(times) / len(times)

        times = []
        for i in range(5):
            start_time = time.time()
            for key in keys:
                double_hash_ht.search(key)
            end_time = time.time()
            times.append(end_time - start_time)
            # double_hash_avg_time = sum(times) / len(times)
        double_hash_y[i] = sum(times) / len(times)

        # Create a chart to compare search times at different load factors
        x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        sep_chain_y = [0] * 10
        linear_probe_y = [0] * 10
        double_hash_y = [0] * 10

        for i in range(5):
            # Instantiate hash tables for each load factor
            sep_chain_ht = HashTableSeparateChaining(int(n / x[i]))
            linear_probe_ht = HashTableLinearProbing(int(n / x[i]))
            double_hash_ht = HashTableDoubleHashing(int(n / x[i]))

            # Insert keys and values into hash tables
            for j in range(5):
                sep_chain_ht.insert(keys[j], values[j])
                linear_probe_ht.insert(keys[j], values[j])
                double_hash_ht.insert(keys[j], values[j])

            # Time the search operation for each load factor
            times = []
            for j in range(5):
                start_time = time.time()
                for key in keys:
                    sep_chain_ht.search(key)
                end_time = time.time()
                times.append(end_time - start_time)
            sep_chain_y[i] = sum(times) / len(times)

            times = []
            for j in range(5):
                start_time = time.time()
                for key in keys:
                    linear_probe_ht.search(key)
                end_time = time.time()
                times.append(end_time - start_time)
            linear_probe_y[i] = sum(times) / len(times)

            times = []
            for j in range(5):
                start_time = time.time()
                for key in keys:
                    double_hash_ht.search(key)
                end_time = time.time()
                times.append(end_time - start_time)
            double_hash_y[i] = sum(times) / len(times)

        # Create a chart to compare search times at different load factors
        plt.plot(x, sep_chain_y, label="Separate Chaining")
        plt.plot(x, linear_probe_y, label="Linear Probing")
        plt.plot(x, double_hash_y, label="Double Hashing")
        plt.title("Average Search Time vs. Load Factor")
        plt.xlabel("Load Factor")
        plt.ylabel("Average Search Time (s)")
        plt.legend()
        plt.show()

        # Print the average search times for each hash table implementation
        print(f"Separate Chaining: {sep_chain_avg_time} s")
        print(f"Linear Probing: {linear_probe_avg_time} s")
        print(f"Double Hashing: {double_hash_avg_time} s")

        return sep_chain_y, linear_probe_y, double_hash_y


print(test(0.1, 10000))

# powinny byc wieksze wartosci / dodac zapisanie wykresu bo dlugo trwa funkcja przy wiekszych
# 5000 , 1.0
# test(1.0, 50)
