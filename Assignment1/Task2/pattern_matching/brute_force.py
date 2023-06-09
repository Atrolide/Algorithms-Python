def brute_force_search(pattern, text):
    m, n = len(text), len(pattern)
    i, j = 0, 0
    last_star, last_text = -1, -1

    while i < m:
        if j < n and pattern[j] == '\\':
            j += 1
            if j == n:
                return False
            if pattern[j] == '?' or pattern[j] == '*':
                if pattern[j] == text[i]:
                    i += 1
                    j += 1
                else:
                    if last_star >= 0:
                        j = last_star + 1
                        last_text += 1
                        i = last_text
                    else:
                        return False
            else:
                if text[i] != pattern[j]:
                    if last_star >= 0:
                        j = last_star + 1
                        last_text += 1
                        i = last_text
                    else:
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
        elif pattern[j] != text[i] and i + n <= m:
            i += 1
        else:
            return False

    while j < n and pattern[j] == '*':
        j += 1

    return j == n

