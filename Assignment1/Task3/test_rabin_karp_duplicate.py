import unittest
from rabin_karp_picture import rabin_karp_duplicate_picture
from random import randint
from time import time

class TestRabinKarp(unittest.TestCase):
    def generate_picture(self, M, N):
        return [[randint(0, 255) for _ in range(N)] for _ in range(M)]

    def duplicate_corner(self, picture, K):
        top_right_corner = [row[-K:] for row in picture[:K]]
        for i in range(K, len(picture)):
            if picture[i-K][:K] == top_right_corner:
                return True
            for j in range(K, len(picture[0])):
                if all(picture[i-k][j-K+jj] == top_right_corner[k][jj] for k in range(K) for jj in range(K)):
                    return True
        return False

    def test_algorithm(self):
        test_cases = [(10, 10, 3), (100, 100, 5), (1000, 1000, 10)]

        for M, N, K in test_cases:
            picture = self.generate_picture(M, N)

            start_time = time()
            expected_result = self.duplicate_corner(picture, K)
            expected_time = time() - start_time

            start_time = time()
            result = rabin_karp_duplicate_picture(picture, K)
            actual_time = time() - start_time

            self.assertEqual(result, expected_result, f"Error: expected {expected_result}, but got {result}")
            self.assertLessEqual(actual_time, expected_time * 10, f"Error: algorithm took too long ({actual_time} seconds)")

if __name__ == "__main__":
    unittest.main()

