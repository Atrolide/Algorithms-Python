import timeit
from Task1.pattern_matching import *
import string
import random

import timeit
from Task1.pattern_matching import *

T = "this is a sample text for pattern matching algorithms"
P = "sample text"

t_binary_sunday = timeit.timeit(lambda: binary_sunday_search(P, T), number=100)
t_gusfield_z = timeit.timeit(lambda: gusfield_z_search(P, T), number=100)
t_kmp = timeit.timeit(lambda: kmp_search(P, T), number=100)
t_rabin_karp = timeit.timeit(lambda: rabin_karp_search(P, T), number=100)

print(f"Binary Sunday: {t_binary_sunday:.5f} seconds")
print(f"Gusfield Z: {t_gusfield_z:.5f} seconds")

if t_binary_sunday < 2 * t_gusfield_z:
    print("Binary Sunday is at least twice as fast as Gusfield Z")
else:
    print("ERROR: Gusfield Z is faster than Binary Sunday")



T = "this is a test string for pattern matching algorithms"
P = "pattern"

t_kmp = timeit.timeit(lambda: kmp_search(P, T), number=100)
t_rabin_karp = timeit.timeit(lambda: rabin_karp_search(P, T), number=100)

print(f"\nKMP: {t_kmp:.5f} seconds")
print(f"Rabin-Karp: {t_rabin_karp:.5f} seconds")

if t_kmp < 2 * t_rabin_karp:
    print("KMP is at least twice as fast as Rabin-Karp")
else:
    print("ERROR: Rabin-Karp is faster than KMP")


T = "this is a sample text for pattern matching algorithms"
P = "this"

t_rabin_karp2 = timeit.timeit(lambda: rabin_karp_search(P, T), number=100)
t_sunday = timeit.timeit(lambda: sunday_search(P, T), number=100)

print(f"\nRabin-Karp: {t_rabin_karp2:.5f} seconds")
print(f"Sunday: {t_sunday:.5f} seconds")

if t_sunday < 2 * t_rabin_karp2:
    print("Sunday is at least twice as fast as Rabin-Karp")
else:
    print("ERROR: Rabin-Karp is faster than Sunday")
