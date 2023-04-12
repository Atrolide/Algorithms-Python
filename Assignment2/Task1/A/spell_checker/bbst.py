from collections import defaultdict
from sortedcontainers import SortedSet


def build_dictionary_bbst(filename):
    with open(filename, 'r') as f:
        words = SortedSet(line.strip() for line in f)
    return words


def spell_check_bbst(text, dictionary):
    misspelled_words = defaultdict(int)
    words = text.split()
    for word in words:
        if word not in dictionary:
            misspelled_words[word] += 1
    return misspelled_words
