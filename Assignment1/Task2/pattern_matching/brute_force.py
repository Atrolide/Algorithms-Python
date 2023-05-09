def brute_force_search(pattern, text):
    m, n = len(text), len(pattern)
    i, j = 0, 0
    last_star, last_text = -1, -1

    while i < m:
        if j < n and pattern[j] == '\\':
            j += 1
            if j == n:
                return False
            if pattern[j] == '*':
                j += 1
                if j == n:
                    return True
                while i < m and text[i] != pattern[j]:
                    i += 1
                if i == m:
                    return False
                last_star = j
                last_text = i
                j += 1
            elif text[i] != pattern[j]:
                return False
            else:
                i += 1
                j += 1
        elif j < n and pattern[j] == '?':
            i += 1
            j += 1
        elif j < n and pattern[j] == '*':
            last_star = j
            last_text = i
            j += 1
        elif j < n and text[i] == pattern[j]:
            i += 1
            j += 1
        elif last_star >= 0:
            j = last_star + 1
            last_text += 1
            i = last_text
        else:
            return False

    while j < n and pattern[j] == '*':
        j += 1

    return j == n