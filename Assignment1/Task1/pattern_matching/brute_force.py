def brute_force_search(pattern, text):
    positions = []
    for i in range(len(text)):
        for j in range(len(pattern)):
            if i + j >= len(text) or text[i + j] != pattern[j]:
                break
        else:
            positions.append(i)
    return positions



'''
def brute_force_search(pattern, text):
    # Create an empty list to store the starting positions of the pattern in the text
    positions = []

    # Iterate over all possible starting positions i in the text where the length of the substring starting at i is at least as long as the pattern
    for i in range(len(text) - len(pattern) + 1):
        # Initialize a counter j to 0
        j = 0
        # While j is less than the length of the pattern and the character at position i + j in the text matches the character at position j in the pattern, increment j
        while j < len(pattern) and text[i + j] == pattern[j]:
            j += 1
        # If j equals the length of the pattern, the pattern has been found at position i in the text. Append i to the positions list.
        if j == len(pattern):
            positions.append(i)

    # Return the list of starting positions of the pattern in the text
    return positions
'''