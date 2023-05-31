import numpy as np

from tables import *

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
