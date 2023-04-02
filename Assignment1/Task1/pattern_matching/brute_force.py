def brute_force_search(pattern, text):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        j = 0
        while j < len(pattern) and text[i + j] == pattern[j]:
            j += 1
        if j == len(pattern):
            positions.append(i)

    print('This is the Brute Force Algorithm!')
    return positions
