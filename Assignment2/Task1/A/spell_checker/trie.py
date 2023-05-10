class TrieNode:
    # Each node in the Trie has an is_word flag and a dictionary of children nodes
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.children = {}


class Trie:
    # The Trie class has a root node
    def __init__(self):
        self.root = TrieNode()

    # Inserts a word into the Trie by traversing through each character in the word
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True


def build_dictionary_trie(words):
    # Builds a new Trie and inserts each word in words into the Trie
    trie = Trie()
    for word in words:
        trie.insert(word.lower())
    return trie


def spell_check_trie(text, trie):
    # Traverses the Trie for each character in the text
    errors = []
    node = trie.root
    node_prefix = ''
    for char in text.lower():
        # When a space is found, the current node is checked for a complete word
        if char == ' ':
            if not node.is_word:
                errors.append(node_prefix)
            node = trie.root
            node_prefix = ''
        elif char in node.children:
            node = node.children[char]
            node_prefix += char
        else:
            node_prefix += char
    # The final node is checked for a complete word
    if not node.is_word:
        errors.append(node_prefix)
    return errors
