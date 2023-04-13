class TrieNode:
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True


def build_dictionary_trie(words):
    trie = Trie()
    for word in words:
        trie.insert(word.lower())
    return trie


def spell_check_trie(text, trie):
    errors = []
    node = trie.root
    node_prefix = ''
    for char in text.lower():
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
    if not node.is_word:
        errors.append(node_prefix)
    return errors
