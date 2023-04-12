def sunday_search(pattern, text):
    n = len(text)
    m = len(pattern)
    if m > n:
        return False
    i = 0
    while i <= n - m:
        j = 0
        while j < m and (text[i+j] == pattern[j] or pattern[j] == '?'):
            j += 1
        if j == m:
            return True
        if pattern[m-1] == '*':
            shift = m - j - 1
            max_shift = n - (i + j)
            i += min(shift, max_shift)
        elif j < m and pattern[j] == '?':
            i += 1
        elif i + m < n and text[i+m] in pattern:
            i += m - pattern.rindex(text[i+m])
        else:
            i += 1
    return False

# TODO: Fix '*' wildcard not working correctly.
