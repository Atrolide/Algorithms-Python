class HashSet:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.table = [None] * capacity

    def add(self, value):
        index = hash(value) % self.capacity
        if self.table[index] is None:
            self.table[index] = [value]
        else:
            if value not in self.table[index]:
                self.table[index].append(value)

    def remove(self, value):
        index = hash(value) % self.capacity
        if self.table[index] is not None:
            try:
                self.table[index].remove(value)
            except ValueError:
                pass

    def __contains__(self, value):
        index = hash(value) % self.capacity
        if self.table[index] is None:
            return False
        else:
            return value in self.table[index]


def build_dictionary_hash(words):
    dictionary = HashSet()
    for word in words:
        dictionary.add(word.lower())
    return dictionary


def spell_check_hash(text, dictionary):
    errors = []
    for word in text.split():
        if word.lower() not in dictionary:
            errors.append(word)
    return errors
