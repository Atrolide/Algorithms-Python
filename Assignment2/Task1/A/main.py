import timeit

from Task1.A.spell_checker import *
from spell_checker import *
import time

english_words = set(word.strip().lower() for word in open('english_words.txt'))

dictionary_naive = build_dictionary_naive(english_words)
dictionary_bbst = build_dictionary_bbst(english_words)
dictionary_hash = build_dictionary_hash(english_words)
dictionary_trie = build_dictionary_trie(english_words)

# misspelled
if spell_check_naive('chuj', dictionary_naive):
    print('misspelled')
else:
    print('ok')

if spell_check_bbst('chuj', dictionary_bbst):
    print('misspelled')
else:
    print('ok')

if spell_check_hash('chuj', dictionary_hash):
    print('misspelled')
else:
    print('ok')

if spell_check_trie('chuj', dictionary_trie):
    print('misspelled')
else:
    print('ok')

# correct
if spell_check_naive('privy', dictionary_naive):
    print('misspelled')
else:
    print('ok')

if spell_check_bbst('privy', dictionary_bbst):
    print('misspelled')
else:
    print('ok')

if spell_check_hash('privy', dictionary_hash):
    print('misspelled')
else:
    print('ok')

if spell_check_trie('privy', dictionary_trie):
    print('misspelled')
else:
    print('ok')

# to do: Compare running times for dictionary building and spell checking on a large piece of text.


naive_running_time_build = timeit.timeit(lambda: build_dictionary_naive(english_words), number=1)
bbst_running_time_build = timeit.timeit(lambda: build_dictionary_bbst(english_words), number=1)
hash_running_time_build = timeit.timeit(lambda: build_dictionary_hash(english_words), number=1)
trie_running_time_build = timeit.timeit(lambda: build_dictionary_trie(english_words), number=1)


print(f"Naive time for dictionary building: {naive_running_time_build}")
print(f"BBST time for dictionary building: {bbst_running_time_build}")
print(f"Hash time for dictionary building: {hash_running_time_build}")
print(f"Trie time for dictionary building: {trie_running_time_build}")
