import timeit
import matplotlib.pyplot as plt

from Task1.A.spell_checker import *
from spell_checker import *

english_words = set(word.strip().lower() for word in open('english_words.txt'))

# Measure the build time for each spell checker implementation
build_times = []
spell_checkers = [
    (build_dictionary_naive, spell_check_naive),
    (build_dictionary_bbst, spell_check_bbst),
    (build_dictionary_hash, spell_check_hash),
    (build_dictionary_trie, spell_check_trie)
]

for build_func, _ in spell_checkers:
    build_start_time = timeit.default_timer()
    dictionary = build_func(english_words)
    build_end_time = timeit.default_timer()
    build_time = build_end_time - build_start_time
    build_times.append(build_time)

# Measure the spell check time for each spell checker implementation

spell_check_times = []

with open('IlliadByHomer2.txt', 'r', encoding='utf-8') as file:
    text = file.read()
dictionary = build_dictionary_naive(english_words)
spell_check_time = timeit.timeit(lambda: spell_check_naive(text, dictionary), number=1, globals=globals())

for _, spell_checker_func in spell_checkers:
    if spell_checker_func == spell_check_trie:
        # Create a Trie object from the dictionary set
        trie = build_dictionary_trie(dictionary)
        spell_check_time = timeit.timeit(lambda: spell_checker_func(text, trie), number=1, globals=globals())
    else:
        spell_check_time = timeit.timeit(lambda: spell_checker_func(text, dictionary), number=1, globals=globals())
    spell_check_times.append(spell_check_time)

# Plotting the graph
labels = ['Naive', 'BBST', 'Hash', 'Trie']
x = range(len(labels))

plt.plot(x, build_times, label='Build Time', marker='o')
plt.plot(x, spell_check_times, label='Spell Check Time', marker='o')

plt.xlabel('Spell Checker')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Spell Checker Performance')
plt.xticks(x, labels)
plt.legend()
plt.grid(True)
plt.show()


