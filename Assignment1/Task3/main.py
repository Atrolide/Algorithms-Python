from rabin_karp_picture import rabin_karp_duplicate_picture
from random import randint
from time import time

def generate_picture(M, N):
    return [[randint(0, 255) for _ in range(N)] for _ in range(M)]

def duplicate_corner(picture, K):
    top_right_corner = [row[-K:] for row in picture[:K]]
    for i in range(K, len(picture)):
        if picture[i-K][:K] == top_right_corner:
            return True
        for j in range(K, len(picture[0])):
            if all(picture[i-k][j-K+jj] == top_right_corner[k][jj] for k in range(K) for jj in range(K)):
                return True
    return False

def test_algorithm(M, N, K):
    picture = generate_picture(M, N)

    start_time = time()
    expected_result = duplicate_corner(picture, K)
    expected_time = time() - start_time

    start_time = time()
    result = rabin_karp_duplicate_picture(picture, K)
    actual_time = time() - start_time

    assert result == expected_result, f"Error: expected {expected_result}, but got {result}"
    assert actual_time <= expected_time * 10, f"Error: algorithm took too long ({actual_time} seconds)"
    print("Test passed successfully!")

if __name__ == "__main__":
    test_algorithm(10, 10, 3)
    test_algorithm(100, 100, 5)
    test_algorithm(1000, 1000, 10)
