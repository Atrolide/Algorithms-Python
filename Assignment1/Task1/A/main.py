from Task1.pattern_matching import *
import timeit
import warnings
import matplotlib.pyplot as plt
import random
import re
from tabulate import tabulate
from termcolor import colored

# Open the text file and read its contents
with open('IlliadByHomer.txt', 'r', encoding='utf-8') as file:
    all_lines = file.readlines()

num_lines = 5000
running_times_list = []
while num_lines < 25000:
    # Read a certain number of lines from the text file
    text = ''.join(all_lines[:num_lines])

    # Find all the sentences in the text
    sentences = re.findall(r'([^.!?]+[.!?])', text)

    # Choose a random 3-sentence pattern
    pattern_start = random.randint(0, len(sentences) - 3)
    pattern_end = pattern_start + 3
    long_pattern = ' '.join(sentences[pattern_start:pattern_end])

    # Measure the running time of each algorithm for the pattern
    bf_running_time = timeit.timeit(lambda: brute_force_search(long_pattern, text), number=1)
    sunday_running_time = timeit.timeit(lambda: sunday_search(long_pattern, text), number=1)
    kmp_running_time = timeit.timeit(lambda: kmp_search(long_pattern, text), number=1)
    fsm_running_time = timeit.timeit(lambda: fsm_search(long_pattern, text), number=1)
    rk_running_time = timeit.timeit(lambda: rabin_karp_search(long_pattern, text), number=1)
    gz_running_time = timeit.timeit(lambda: gusfield_z_search(long_pattern, text), number=1)

    # Check if the pattern was found
    if not bf_running_time and not sunday_running_time and not kmp_running_time and not fsm_running_time and not rk_running_time and not gz_running_time:
        raise ValueError("Pattern not found in the text")

    # Append the running times to the list
    running_times_list.append([bf_running_time, sunday_running_time, kmp_running_time, fsm_running_time, rk_running_time, gz_running_time])

    num_lines += 5000

    print(f"\nNumber of lines: {num_lines} \n")
    print(f"\nRandomly chosen pattern:\n {long_pattern}\n")
    headers = ['Algorithm', 'Running Time (seconds)']
    table = []
    for i, algorithm in enumerate(['Brute Force', 'Sunday', 'KMP', 'FSM', 'Rabin-Karp', 'Gusfield-Z']):
        color = 'green' if running_times_list[-1][i] == min(running_times_list[-1]) else 'white'
        table.append([colored(algorithm, color), colored(f"{running_times_list[-1][i]:.5f}", color)])
    print(tabulate(table, headers=headers, tablefmt='grid'))

# Filter out the deprecation warning
warnings.filterwarnings("ignore", message="Support for FigureCanvases without a required_interactive_framework attribute was deprecated")

# Plot the running time of each algorithm for the pattern
algorithms = ['Brute Force', 'Sunday', 'KMP', 'FSM', 'Rabin-Karp', 'Gusfield-Z']
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown']

fig, ax = plt.subplots()
for i in range(len(algorithms)):
    ax.plot(range(5000, 25000, 5000), [running_times[i] for running_times in running_times_list], marker='o', color=colors[i], label=algorithms[i])
    for j in range(len(range(5000, 25000, 5000))):
        ax.annotate(f"{running_times_list[j][i]:.3f}", xy=(range(5000, 25000, 5000)[j], running_times_list[j][i]), xytext=(8,-10), textcoords='offset points', color=colors[i])


plt.xlabel('Number of Lines')
plt.ylabel('Running Time (seconds)')
plt.title('Running Time of Pattern Matching Algorithms for Patterns of Increasing Length')
plt.legend()
plt.show()

