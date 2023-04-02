def sunday_search(pattern, text):
    # Create a dictionary to store the shifts for each character in the pattern
    shifts = {}
    # Iterate over the characters in the pattern from right to left
    for i in range(len(pattern) - 1, -1, -1):
        # If the character is not already in the shifts dictionary, add it with the shift value
        if pattern[i] not in shifts:
            # The shift value is the distance from the right end of the pattern to the last occurrence of the character
            shifts[pattern[i]] = len(pattern) - i
    # Add a shift value for the wildcard character '*'
    shifts['*'] = len(pattern) + 1

    # Initialize variables for the loop
    i = 0
    positions = []

    # Loop over the text, checking for matches with the pattern
    while i <= len(text) - len(pattern):
        # Initialize a counter for the characters matched so far
        j = 0
        # Check for matches at each position in the pattern
        while j < len(pattern) and text[i + j] == pattern[j]:
            j += 1
        # If the entire pattern was matched, add the starting position to the list of positions
        if j == len(pattern):
            positions.append(i)
        # If the end of the text has been reached, exit the loop
        if i + len(pattern) == len(text):
            break
        # Look up the next character in the text in the shifts dictionary to determine the shift
        next_char = text[i + len(pattern)]
        if next_char in shifts:
            shift = shifts[next_char]
        else:
            shift = shifts['*']
        # Increment i by the shift value
        i += shift

    # Return the list of positions where the pattern was found
    return positions
