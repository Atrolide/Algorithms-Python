def kmp_search(pattern, text):
    # Compute the prefix function of the pattern
    m = len(pattern)  # Length of pattern
    pi = [0] * m  # Initialize prefix function list to all zeros
    j = 0  # Current match position in pattern
    for i in range(1, m):
        # Update j using prefix function until a valid match position is found
        while j > 0 and pattern[j] != pattern[i]:
            j = pi[j - 1]
        # If the characters match, increment j and update prefix function
        if pattern[j] == pattern[i]:
            j += 1
        pi[i] = j  # Store current match position in prefix function

    # Perform the KMP search
    n = len(text)  # Length of text
    j = 0  # Current match position in pattern
    positions = []  # List of match positions
    for i in range(n):
        # Update j using prefix function until a valid match position is found
        while j > 0 and pattern[j] != text[i]:
            j = pi[j - 1]
        # If the characters match, increment j
        if pattern[j] == text[i]:
            j += 1
        # If a match is found, add the index of the first character of the match to the list
        if j == m:
            positions.append(i - m + 1)
            j = pi[j - 1]  # Update j using prefix function for next match
    # Return the list of match positions
    return positions
