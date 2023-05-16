def sunday_search(pattern, text):
    text_length = len(text)
    pattern_length = len(pattern)
    i = 0  # Index for text
    j = 0  # Index for pattern

    # Generate shift table
    shift_table = {}
    for k in range(pattern_length - 1, -1, -1):
        if pattern[k] not in shift_table:
            shift_table[pattern[k]] = pattern_length - k - 1

    while i < text_length:
        if j == pattern_length:
            # Reached the end of pattern, match found
            return True

        if pattern[j] == '*':
            # Wildcard found, check all possible matches for the sequence of characters after the wildcard
            j += 1
            if j == pattern_length:
                # Wildcard is the last character in pattern, match found
                return True
            for k in range(i, text_length):
                if sunday_search(pattern[j:], text[k:]):
                    # Match found after the wildcard, return True
                    return True

            # No match found after the wildcard, return False
            return False

        elif pattern[j] == '?':
            # Wildcard found, matches any single character in text
            if i < text_length:
                i += 1
                j += 1

        elif pattern[j] == '\\':
            # Check if the next character after backslash is a wildcard
            if j + 1 < pattern_length and pattern[j + 1] in ['*', '?']:
                # Backslash followed by wildcard, treat it as a regular character
                if i < text_length and text[i] == pattern[j + 1]:
                    # Match found, move to next character in both text and pattern
                    i += 1
                    j += 2
                else:
                    # Mismatch, no match found
                    return False
            else:
                # Backslash followed by a character, treat it as a regular character
                if i < text_length and text[i] == pattern[j]:
                    # Match found, move to next character in both text and pattern
                    i += 1
                    j += 1
                else:
                    # Mismatch, no match found
                    return False

        elif i < text_length and text[i] == pattern[j]:
            i += 1
            j += 1

        else:
            if j == 0:
                i += 1  # No match at first character of pattern, shift by one (bad character rule)
            elif j == 1 or (j > 1 and pattern[0:j-1] not in text[i-j+1:i]):
                i += shift_table.get(text[i], pattern_length)  # Shift by length of matched prefix plus one (good suffix rule)
                j = 0

    if j == pattern_length:
        # Reached the end of pattern, match found
        return True

    else:
        # Match not found
        return False
