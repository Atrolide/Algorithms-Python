class HashSet:
    def __init__(self, capacity=1000):
        # Initialize the hash set with a specified capacity
        self.capacity = capacity
        # Create a list of None objects with the specified capacity to represent the hash table
        self.table = [None] * capacity

    def add(self, value):
        # Compute the hash code of the value and get its index in the hash table
        index = hash(value) % self.capacity
        # If the index is empty, create a new list with the value and add it to the hash table
        if self.table[index] is None:
            self.table[index] = [value]
        # If the index already has a list, check if the value is already in the list
        else:
            # If the value is not in the list, add it to the end of the list
            if value not in self.table[index]:
                self.table[index].append(value)

    def remove(self, value):
        # Compute the hash code of the value and get its index in the hash table
        index = hash(value) % self.capacity
        # If the index is not empty, try to remove the value from the list at the index
        if self.table[index] is not None:
            try:
                self.table[index].remove(value)
            except ValueError:
                # If the value is not in the list, do nothing
                pass

    def __contains__(self, value):
        # Compute the hash code of the value and get its index in the hash table
        index = hash(value) % self.capacity
        # If the index is empty, the value is not in the hash set
        if self.table[index] is None:
            return False
        # If the index has a list, check if the value is in the list
        else:
            return value in self.table[index]


def build_dictionary_hash(words):
    # Create a new hash set to represent the dictionary
    dictionary = HashSet()
    # For each word in the list of words, add its lowercase version to the dictionary hash set
    for word in words:
        dictionary.add(word.lower())
    # Return the dictionary hash set
    return dictionary


def spell_check_hash(text, dictionary):
    # Create an empty list to store the misspelled words
    errors = []
    # Split the text into words and check each word against the dictionary hash set
    for word in text.split():
        # If the lowercase version of the word is not in the dictionary hash set, add it to the errors list
        if word.lower() not in dictionary:
            errors.append(word)
    # Return the list of misspelled words
    return errors
