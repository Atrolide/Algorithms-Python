def brute_force_search (pattern, text):
    m, n = len(text), len(pattern)
    i, j = 0, 0
    while i < m and j < n:
        if pattern[j] == '\\':
            j += 1
            if j == n:
                return False
            if text[i] != pattern[j]:
                return False
        elif pattern[j] == '?':
            i += 1
            j += 1
        elif pattern[j] == '*':
            j += 1
            if j == n:
                return True
            while i < m and text[i] != pattern[j] and pattern[j] != '?':
                i += 1
            if i == m:
                return False
        elif text[i] != pattern[j]:
            return False
        else:
            i += 1
            j += 1
    if j == n and i == m:
        return True
    if j < n and pattern[j] == '*':
        j += 1
    return j == n and i == m
