def brute_force_search(pattern, text):
    n = len(text)
    m = len(pattern)
    i = 0
    while i <= n - m:
        j = 0
        while j < m and (text[i+j] == pattern[j] or pattern[j] == '?'):
            j += 1
        if j == m:
            return True
        if pattern[j:j+1] == '*':
            k = i + j
            while k <= n:
                if brute_force_search(pattern[j+1:], text[k:]):
                    return True
                k += 1
        i += 1
    return False
