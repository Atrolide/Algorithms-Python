from Task2.pattern_matching import *

def test_algorithms(pattern, text):
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Brute-Force Match Found: {brute_force_search(pattern, text)}")
    print(f"Sunday Match Found: {sunday_search(pattern, text)}")
    print("=" * 50)

if __name__ == "__main__":
    pattern1 = "aba"
    text1 = "aba"
    test_algorithms(pattern1, text1)



