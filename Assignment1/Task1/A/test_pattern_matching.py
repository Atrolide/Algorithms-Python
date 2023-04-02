from Task1.pattern_matching import *
import unittest

class TestPatternMatching(unittest.TestCase):

    def setUp(self):
        with open('IlliadByHomer.txt', 'r', encoding='utf-8') as file:
            self.text = file.read()

    def test_brute_force_search(self):
        pattern = "Let fierce Achilles, dreadful in his rage,"
        positions = brute_force_search(pattern, self.text)
        self.assertEqual(len(positions), 1)
        self.assertEqual(self.text.count('\n', 0, positions[0]) + 1, 2276)

    def test_sunday_search(self):
        pattern = "Let fierce Achilles, dreadful in his rage,"
        positions = sunday_search(pattern, self.text)
        self.assertEqual(len(positions), 1)
        self.assertEqual(self.text.count('\n', 0, positions[0]) + 1, 2276)

    def test_kmp_search(self):
        pattern = "Let fierce Achilles, dreadful in his rage,"
        positions = kmp_search(pattern, self.text)
        self.assertEqual(len(positions), 1)
        self.assertEqual(self.text.count('\n', 0, positions[0]) + 1, 2276)

    def test_fsm_search(self):
        pattern = "Let fierce Achilles, dreadful in his rage,"
        positions = fsm_search(pattern, self.text)
        self.assertEqual(len(positions), 1)
        self.assertEqual(self.text.count('\n', 0, positions[0]) + 1, 2276)

    def test_rabin_karp_search(self):
        pattern = "Let fierce Achilles, dreadful in his rage,"
        positions = rabin_karp_search(pattern, self.text)
        self.assertEqual(len(positions), 1)
        self.assertEqual(self.text.count('\n', 0, positions[0]) + 1, 2276)

    def test_gusfield_z_search(self):
        pattern = "Let fierce Achilles, dreadful in his rage,"
        positions = gusfield_z_search(pattern, self.text)
        self.assertEqual(len(positions), 1)
        self.assertEqual(self.text.count('\n', 0, positions[0]) + 1, 2276)

if __name__ == '__main__':
    unittest.main()
