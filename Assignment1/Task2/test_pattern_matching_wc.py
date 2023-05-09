import unittest
from Task2.pattern_matching import brute_force_search, sunday_search

class TestPatternMatching(unittest.TestCase):
    def test_1(self):
        pattern = "hello*world"
        text = "hellobeautifulworld"
        self.assertTrue(brute_force_search(pattern, text))
        self.assertTrue(sunday_search(pattern, text))

    def test_2(self):
        pattern = "helloworld"
        text = "helloworld"
        self.assertTrue(brute_force_search(pattern, text))
        self.assertTrue(sunday_search(pattern, text))

    def test_3(self):
        pattern = "abcde*fgh?i"
        text = "abcdefgabcdefghi"
        self.assertFalse(brute_force_search(pattern, text))
        self.assertFalse(sunday_search(pattern, text))

    def test_4(self):
        pattern = "a?e"
        text = "ace"
        self.assertTrue(brute_force_search(pattern, text))
        self.assertTrue(sunday_search(pattern, text))

    def test_5(self):
        pattern = "he?lo*w*ld"
        text = "he?lo*world"
        self.assertTrue(brute_force_search(pattern, text))
        self.assertTrue(sunday_search(pattern, text))

    def test_6(self):
        pattern = "Cotam\?"
        text = "Cotam?"
        self.assertTrue(brute_force_search(pattern, text))
        self.assertTrue(sunday_search(pattern, text))

    def test_7(self):
        pattern = "ab*cde?fg"
        text = "abxcdeyfg"
        self.assertTrue(brute_force_search(pattern, text))
        self.assertTrue(sunday_search(pattern, text))

    def test_8(self):
        pattern = "a*b\*c\?d"
        text = "axbybc?d"
        self.assertFalse(brute_force_search(pattern, text))
        self.assertFalse(sunday_search(pattern, text))

    def test_9(self):
        pattern = "a*b\*c?d"
        text = "axbyb*czd"
        self.assertTrue(brute_force_search(pattern, text))
        self.assertTrue(sunday_search(pattern, text))

    def test_10(self):
        pattern = "a\*b"
        text = "a*b"
        self.assertTrue(brute_force_search(pattern, text))
        self.assertTrue(sunday_search(pattern, text))

    def test_11(self):
        pattern = "a\?b"
        text = "a?b"
        self.assertTrue(brute_force_search(pattern, text))
        self.assertTrue(sunday_search(pattern, text))

    def test_12(self):
        pattern = "ab*cd"
        text = "abyyycd"
        self.assertTrue(brute_force_search(pattern, text))
        self.assertTrue(sunday_search(pattern, text))

    def test_13(self):
        pattern = "ab*cd"
        text = "abyyycyycd"
        self.assertTrue(brute_force_search(pattern, text))
        self.assertTrue(sunday_search(pattern, text))



if __name__ == '__main__':
    unittest.main()
