from Task1.pattern_matching import *
import timeit
import warnings
import matplotlib.pyplot as plt

# Open the text file and read its contents
with open('IlliadByHomer.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Define the pattern to search for
pattern = "“God of the silver bow, thy ear incline,"

# Measure the running time of each algorithm
bf_running_time = timeit.timeit(lambda: brute_force_search(pattern, text), number=1)
sunday_running_time = timeit.timeit(lambda: sunday_search(pattern, text), number=1)
kmp_running_time = timeit.timeit(lambda: kmp_search(pattern, text), number=1)
fsm_running_time = timeit.timeit(lambda: fsm_search(pattern, text), number=1)
rk_running_time = timeit.timeit(lambda: rabin_karp_search(pattern, text), number=1)
gz_running_time = timeit.timeit(lambda: gusfield_z_search(pattern, text), number=1)

# Check if the pattern was found
if not bf_running_time and not sunday_running_time and not kmp_running_time and not fsm_running_time and not rk_running_time and not gz_running_time:
    raise ValueError("Pattern not found in the text")

# Filter out the deprecation warning
warnings.filterwarnings("ignore", message="Support for FigureCanvases without a required_interactive_framework attribute was deprecated")

print(f"Brute force running time: {bf_running_time:.5f} seconds")
print(f"Sunday running time: {sunday_running_time:.5f} seconds")
print(f"KMP running time: {kmp_running_time:.5f} seconds")
print(f"FSM running time: {fsm_running_time:.5f} seconds")
print(f"Rabin-Karp running time: {rk_running_time:.5f} seconds")
print(f"Gusfield-Z running time: {gz_running_time:.5f} seconds")