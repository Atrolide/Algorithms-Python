def sunday_algorithm(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < text_length:
        if pattern[j] == '*':
            # Wildcard found, check if it matches any sequence of characters in text
            j += 1
            if j == pattern_length:
                # Wildcard is the last character in pattern, match found
                return True
            while i < text_length and text[i] != pattern[j]:
                i += 1
            if i == text_length:
                # Reached the end of text, no match found
                return False
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if i + pattern_length < text_length:
                # Check if the next character in text matches the first character in pattern
                next_char = text[i + pattern_length]
                if next_char in pattern:
                    i += pattern_length - pattern.find(next_char)
                else:
                    i += pattern_length + 1
            else:
                # Reached the end of text, no match found
                return False

    if j == pattern_length:
        # Reached the end of pattern, match found
        return True
    else:
        # Match not found
        return False



# Example usage
text = "hellodupaworld"
pattern = "hello*world"
result = sunday_algorithm(text, pattern)
print(f"Pattern: {pattern}")
print(f"Text: {text}")
print(result)  # Output: True
print("=" * 50)
