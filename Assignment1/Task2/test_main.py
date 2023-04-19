def test_algorithms(pattern, text):
    print("Pattern: ", pattern)
    print("Text: ", text)
    print("Sunday algorithm: ", sunday_algorithm(pattern, text))
    print("Brute force algorithm: ", brute_force_algorithm(pattern, text))

def sunday_algorithm(pattern, text):
    m = len(pattern)
    n = len(text)
    i = 0
    while i <= n - m:
        j = 0
        while j < m and pattern[j] == text[i + j]:
            j += 1
        if j == m:
            return True
        if i + m == n:
            return False
        i += m - min(j, 1 + pattern.rfind(text[i + m]))
    return False

def brute_force_algorithm(pattern, text):
    if pattern == "" or text == "":
        return False
    if pattern == "*" or pattern == "?":
        return True
    if pattern[0] == "*":
        for i in range(len(text)):
            if brute_force_algorithm(pattern[1:], text[i:]):
                return True
        return False
    if pattern[0] == "?":
        return brute_force_algorithm(pattern[1:], text[1:])
    if pattern[0] == text[0]:
        return brute_force_algorithm(pattern[1:], text[1:])
    else:
        return False

pattern1 = "hello*world"
text1 = "hellobeautifulworld"
test_algorithms(pattern1, text1)