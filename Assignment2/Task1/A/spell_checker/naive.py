def build_dictionary_naive(words):
    return set(words)


def spell_check_naive(text, dictionary):
    errors = []
    for word in text.split():
        if word.lower() not in dictionary:
            errors.append(word)
    return errors
