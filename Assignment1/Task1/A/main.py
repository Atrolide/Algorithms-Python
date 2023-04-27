# TODO: zrobić loop gdzie mierzony tekst będzie coraz wiekszy, zrobić żeby algorytm szukał dalej tesktu

from Task1.pattern_matching import *
import timeit
import warnings
import matplotlib.pyplot as plt

# Open the text file and read its contents
with open('IlliadByHomer.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Define the short and long patterns to search for
short_pattern = "At every rite his share should be increased,\
And his the foremost honours of the feast."
long_pattern = "Lie there, Otryntides! the Trojan earth\
Receives thee dead, though Gygae boast thy birth;\
Those beauteous fields where Hyllus’ waves are roll’d,\
And plenteous Hermus swells with tides of gold,\
Are thine no more.”—The insulting hero said,\
And left him sleeping in eternal shade.\
The rolling wheels of Greece the body tore,\
And dash’d their axles with no vulgar gore."


# Measure the running time of each algorithm for each pattern

bf_running_time_short = timeit.timeit(lambda: brute_force_search(short_pattern, text), number=1)
sunday_running_time_short = timeit.timeit(lambda: sunday_search(short_pattern, text), number=1)
kmp_running_time_short = timeit.timeit(lambda: kmp_search(short_pattern, text), number=1)
fsm_running_time_short = timeit.timeit(lambda: fsm_search(short_pattern, text), number=1)
rk_running_time_short = timeit.timeit(lambda: rabin_karp_search(short_pattern, text), number=1)
gz_running_time_short = timeit.timeit(lambda: gusfield_z_search(short_pattern, text), number=1)

# Check if the short pattern was found
if not bf_running_time_short and not sunday_running_time_short and not kmp_running_time_short and not fsm_running_time_short and not rk_running_time_short and not gz_running_time_short:
    raise ValueError("Short pattern not found in the text")

bf_running_time_long = timeit.timeit(lambda: brute_force_search(long_pattern, text), number=1)
sunday_running_time_long = timeit.timeit(lambda: sunday_search(long_pattern, text), number=1)
kmp_running_time_long = timeit.timeit(lambda: kmp_search(long_pattern, text), number=1)
fsm_running_time_long = timeit.timeit(lambda: fsm_search(long_pattern, text), number=1)
rk_running_time_long = timeit.timeit(lambda: rabin_karp_search(long_pattern, text), number=1)
gz_running_time_long = timeit.timeit(lambda: gusfield_z_search(long_pattern, text), number=1)

# Check if the long pattern was found
if not bf_running_time_long and not sunday_running_time_long and not kmp_running_time_long and not fsm_running_time_long and not rk_running_time_long and not gz_running_time_long:
    raise ValueError("Long pattern not found in the text")

# Filter out the deprecation warning
warnings.filterwarnings("ignore", message="Support for FigureCanvases without a required_interactive_framework attribute was deprecated")

# Plot the running time of each algorithm for each pattern
algorithms = ['Brute Force', 'Sunday', 'KMP', 'FSM', 'Rabin-Karp', 'Gusfield-Z']
short_running_times = [bf_running_time_short, sunday_running_time_short, kmp_running_time_short, fsm_running_time_short, rk_running_time_short, gz_running_time_short]
long_running_times = [bf_running_time_long, sunday_running_time_long, kmp_running_time_long, fsm_running_time_long, rk_running_time_long, gz_running_time_long]

fig, ax = plt.subplots()
ax.plot(algorithms, short_running_times, marker='o', label='Short Pattern')
ax.plot(algorithms, long_running_times, marker='o', label='Long Pattern')
plt.xlabel('Algorithm')
plt.ylabel('Running Time (seconds)')
plt.title('Running Time of Pattern Matching Algorithms for Short and Long Patterns')
plt.legend()
plt.show()
plt.savefig('pattern_matching.png')


print(f"Short pattern:")
print(f"Brute force running time: {bf_running_time_short:.5f} seconds")
print(f"Sunday running time: {sunday_running_time_short:.5f} seconds")
print(f"KMP running time: {kmp_running_time_short:.5f} seconds")
print(f"FSM running time: {fsm_running_time_short:.5f} seconds")
print(f"Rabin-Karp running time: {rk_running_time_short:.5f} seconds")
print(f"Gusfield-Z running time: {gz_running_time_short:.5f} seconds")

print(f"\nLong pattern:")
print(f"Brute force running time: {bf_running_time_long:.5f} seconds")
print(f"Sunday running time: {sunday_running_time_long:.5f} seconds")
print(f"KMP running time: {kmp_running_time_long:.5f} seconds")
print(f"FSM running time: {fsm_running_time_long:.5f} seconds")
print(f"Rabin-Karp running time: {rk_running_time_long:.5f} seconds")
print(f"Gusfield-Z running time: {gz_running_time_long:.5f} seconds")

