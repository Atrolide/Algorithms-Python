import timeit
from Task1.pattern_matching import *
import string
import random

T = ''.join(random.choices(string.ascii_lowercase, k=100000))
P = T[5000:7000]

t_binary_sunday = timeit.timeit(lambda: binary_sunday_search(P, T), number=100)
t_gusfield_z = timeit.timeit(lambda: gusfield_z_search(P, T), number=100)
t_kmp = timeit.timeit(lambda: kmp_search(P, T), number=100)
t_rabin_karp = timeit.timeit(lambda: rabin_karp_search(P, T), number=100)
t_sunday = timeit.timeit(lambda: sunday_search(P, T), number=100)

print(f"Binary Sunday: {t_binary_sunday:.5f} seconds")
print(f"Gusfield Z: {t_gusfield_z:.5f} seconds")

if t_binary_sunday < 2 * t_gusfield_z:
    print("Binary Sunday is at least twice as fast as Gusfield Z")
else:
    print("ERROR: Gusfield Z is faster than Binary Sunday")

print(f"\nKMP: {t_kmp:.5f} seconds")
print(f"Rabin-Karp: {t_rabin_karp:.5f} seconds")

if t_kmp < 2 * t_rabin_karp:
    print("KMP is at least twice as fast as Rabin-Karp")
else:
    print("ERROR: Rabin-Karp is faster than KMP")

T = ''.join(random.choices(string.ascii_lowercase, k=10000))
pattern = ''.join(random.choices(string.ascii_lowercase, k=100))
P = pattern + ''.join([''.join(random.choices(string.ascii_lowercase, k=1000)) + pattern for _ in range(99)])
t_rabin_karp2 = timeit.timeit(lambda: rabin_karp_search(P, T), number=100)
t_sunday2 = timeit.timeit(lambda: sunday_search(P, T), number=100)

print(f"\nRabin-Karp: {t_rabin_karp2:.5f} seconds")
print(f"Sunday: {t_sunday2:.5f} seconds")

if t_rabin_karp2 < 2 * t_sunday2:
    print("Rabin-Karp is at least twice as fast as Sunday")
else:
    print("ERROR: Sunday is faster than Rabin-Karp")