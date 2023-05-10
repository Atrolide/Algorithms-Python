from collections import defaultdict
from sortedcontainers import SortedSet


def build_dictionary_bbst(words):
    words = SortedSet(line.strip() for line in words)  # create a SortedSet of words from the input lines
    return words  # return the SortedSet of words


def spell_check_bbst(text, dictionary):
    misspelled_words = defaultdict(int)  # create a default dict to store misspelled words
    words = text.split()  # split the input text into words
    for word in words:  # loop over each word in the text
        if word not in dictionary:  # check if the word is in the dictionary (SortedSet)
            misspelled_words[word] += 1  # if not, increment the count of misspelled words
    return misspelled_words  # return the default dict of misspelled words
