def binary_sunday_search(P, T):
    m, n = len(P), len(T)
    skip = {c: m - i - 1 for i, c in enumerate(P[:m - 1])}
    i = 0
    while i <= n - m:
        j = 0
        while T[i + j] == P[j]:
            j += 1
            if j >= m:
                return i
        i += skip.get(T[i + m], m)
    return -1