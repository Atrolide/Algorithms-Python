from rabin_karp_picture import rabin_karp_duplicate_picture
from random import randint
from time import time

# Define a function named generate_picture that generates a random picture of size M x N.
def generate_picture(M, N):
    # Use a nested list comprehension to generate a random picture of size M x N.
    return [[randint(0, 255) for _ in range(N)] for _ in range(M)]

# Define a function named duplicate_corner that checks if there is a duplicated corner of size K in a given picture.
def duplicate_corner(picture, K):
    # Extract the top-right corner of size K from the picture.
    top_right_corner = [row[-K:] for row in picture[:K]]
    # Iterate over the remaining rows in the picture.
    for i in range(K, len(picture)):
        # If the top-right corner matches the top-left corner of the current row, then there is a duplicated corner.
        if picture[i-K][:K] == top_right_corner:
            return True
        # Iterate over the remaining columns in the current row.
        for j in range(K, len(picture[0])):
            # Check if the current KxK sub-picture matches the top-right corner.
            if all(picture[i-k][j-K+jj] == top_right_corner[k][jj] for k in range(K) for jj in range(K)):
                return True
    # If no duplicated corner is found, return False.
    return False

# Define a function that generates a random picture and tests if the duplicate_corner function and the rabin_karp_duplicate_picture function return the same result.
def test_algorithm(M, N, K):
    # Generate a random picture of size M x N.
    picture = generate_picture(M, N)

    # Measure the time it takes to run the duplicate_corner function on the picture.
    start_time = time()
    expected_result = duplicate_corner(picture, K)
    expected_time = time() - start_time

    # Measure the time it takes to run the rabin_karp_duplicate_picture function on the picture.
    start_time = time()
    result = rabin_karp_duplicate_picture(picture, K)
    actual_time = time() - start_time

    # Assert that the result of the rabin_karp_duplicate_picture function matches the expected result of the duplicate_corner function.
    assert result == expected_result, f"Error: expected {expected_result}, but got {result}"
    # Assert that the actual time it took to run the rabin_karp_duplicate_picture function is less than or equal to 10 times the time it took to run the duplicate_corner function.
    assert actual_time <= expected_time * 10, f"Error: algorithm took too long ({actual_time} seconds)"
    # Print a success message if both assertions pass.
    print("Test passed successfully!")

# If the module is being run as the main program, run three tests on pictures of different sizes.
if __name__ == "__main__":
    test_algorithm(10, 10, 3)
    test_algorithm(100, 100, 5)
    test_algorithm(1000, 1000, 10)
