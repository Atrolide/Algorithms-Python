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
if spell_check_naive('gdfgfdgfd', dictionary_naive):
    print('misspelled')
else:
    print('ok')

if spell_check_bbst('gdfgfdgfd', dictionary_bbst):
    print('misspelled')
else:
    print('ok')

if spell_check_hash('gdfgfdgfd', dictionary_hash):
    print('misspelled')
else:
    print('ok')

if spell_check_trie('gdfgfdgfd', dictionary_trie):
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

naive_running_time_build = timeit.timeit(lambda: build_dictionary_naive(english_words), number=1)
bbst_running_time_build = timeit.timeit(lambda: build_dictionary_bbst(english_words), number=1)
hash_running_time_build = timeit.timeit(lambda: build_dictionary_hash(english_words), number=1)
trie_running_time_build = timeit.timeit(lambda: build_dictionary_trie(english_words), number=1)

print(f"Naive time for dictionary building: {naive_running_time_build}")
print(f"BBST time for dictionary building: {bbst_running_time_build}")
print(f"Hash time for dictionary building: {hash_running_time_build}")
print(f"Trie time for dictionary building: {trie_running_time_build}")

naive_running_time_check_correct = timeit.timeit(lambda: spell_check_naive('privy', dictionary_naive), number=1)
bbst_running_time_check_correct = timeit.timeit(lambda: spell_check_bbst('privy', dictionary_bbst), number=1)
hash_running_time_check_correct = timeit.timeit(lambda: spell_check_hash('privy', dictionary_hash), number=1)
trie_running_time_check_correct = timeit.timeit(lambda: spell_check_trie('privy', dictionary_trie), number=1)

print('')

print(f"Naive time for finding correct word: {naive_running_time_check_correct}")
print(f"BBST time for finding correct word: {bbst_running_time_check_correct}")
print(f"Hash time for finding correct word: {hash_running_time_check_correct}")
print(f"trie time for finding correct word: {trie_running_time_check_correct}")

naive_running_time_check_wrong = timeit.timeit(lambda: spell_check_naive('gdfgfdgfd', dictionary_naive), number=1)
bbst_running_time_check_wrong = timeit.timeit(lambda: spell_check_bbst('gdfgfdgfd', dictionary_bbst), number=1)
hash_running_time_check_wrong = timeit.timeit(lambda: spell_check_hash('gdfgfdgfd', dictionary_hash), number=1)
trie_running_time_check_wrong = timeit.timeit(lambda: spell_check_trie('gdfgfdgfd', dictionary_trie), number=1)

print('')

print(f"Naive time for finding misspelled word: {naive_running_time_check_wrong}")
print(f"BBST time for finding misspelled word: {bbst_running_time_check_wrong}")
print(f"Hash time for finding misspelled word: {hash_running_time_check_wrong}")
print(f"trie time for finding misspelled word: {trie_running_time_check_wrong}")

naive_running_time_check_correct = timeit.timeit(lambda: spell_check_naive('abashing', dictionary_naive), number=1)
bbst_running_time_check_correct = timeit.timeit(lambda: spell_check_bbst('abashing', dictionary_bbst), number=1)
hash_running_time_check_correct = timeit.timeit(lambda: spell_check_hash('abashing', dictionary_hash), number=1)
trie_running_time_check_correct = timeit.timeit(lambda: spell_check_trie('abashing', dictionary_trie), number=1)

print('')

print(f"Naive time for finding correct word: {naive_running_time_check_correct}")
print(f"BBST time for finding correct word: {bbst_running_time_check_correct}")
print(f"Hash time for finding correct word: {hash_running_time_check_correct}")
print(f"trie time for finding correct word: {trie_running_time_check_correct}")
