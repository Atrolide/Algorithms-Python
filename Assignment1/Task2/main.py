from Task2.pattern_matching import *

def test_algorithms(pattern, text):
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Brute-Force Match Found: {brute_force_search(pattern, text)}")
    print(f"Sunday Match Found: {sunday_search(pattern, text)}")
    print("=" * 50)

if __name__ == "__main__":
    pattern1 = "hello*world"
    text1 = "hellobeautifulworld"
    test_algorithms(pattern1, text1)

    pattern2 = "helloworld"
    text2 = "helloworld"
    test_algorithms(pattern2, text2)


    pattern3 = "abcde*fgh?i"
    text3 = "abcdefgabcdefghi"
    test_algorithms(pattern3, text3)

    pattern4 = "a?e"
    text4 = "ace"
    test_algorithms(pattern4, text4)

    pattern5 = "he?lo*w*ld"
    text5 = "he?lo*world"
    test_algorithms(pattern5, text5)

    pattern6 = "Cotam\?"
    text6 = "Cotam?"
    test_algorithms(pattern6, text6)

    pattern7 = "*\\**"
    text7 = "foo\*bar\baz"
    test_algorithms(pattern7, text7)

    pattern8 = "ab*cde?fg"
    text8 = "abxcdeyfg"
    test_algorithms(pattern8, text8)

    pattern9 = "a*b\*c\?d"
    text9 = "axbybc?d"
    test_algorithms(pattern9, text9)

    pattern10 = "a*b\*c?d"
    text10 = "axbyb*czd"
    test_algorithms(pattern10, text10)

    pattern11 = "a\*b"
    text11 = "a*b"
    test_algorithms(pattern11, text11)

    pattern12 = "a\?b"
    text12 = "a?b"
    test_algorithms(pattern12, text12)

