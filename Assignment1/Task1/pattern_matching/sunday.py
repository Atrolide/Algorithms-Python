def sunday_search(pattern, text):
    shifts = {}
    for i in range(len(pattern) - 1, -1, -1):
        if pattern[i] not in shifts:
            shifts[pattern[i]] = len(pattern) - i
    shifts['*'] = len(pattern) + 1

    # Initialize variables
    i = 0
    positions = []

    while i <= len(text) - len(pattern):
        j = 0
        while j < len(pattern) and text[i + j] == pattern[j]:
            j += 1
        if j == len(pattern):
            positions.append(i)
        if i + len(pattern) == len(text):
            break
        next_char = text[i + len(pattern)]
        if next_char in shifts:
            shift = shifts[next_char]
        else:
            shift = shifts['*']
        i += shift

    print('This is the Sunday Algorithm!')
    return positions
