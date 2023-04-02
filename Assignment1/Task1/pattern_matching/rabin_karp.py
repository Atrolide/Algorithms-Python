def rabin_karp_search(pattern, text):
    p = len(pattern)
    t = len(text)
    result = []
    if p > t:
        return result

    # Choose a prime number and a base for hashing
    prime = 101
    base = 256

    # Calculate hash values for pattern and the first window of text
    pattern_hash = 0
    window_hash = 0
    for i in range(p):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % prime
        window_hash = (window_hash * base + ord(text[i])) % prime

    # Slide the pattern over the text, rehashing the window each time
    for i in range(t - p + 1):
        if pattern_hash == window_hash and pattern == text[i:i + p]:
            result.append(i)

        # Calculate the hash value for the next window of text
        if i < t - p:
            window_hash = (base * (window_hash - ord(text[i]) * pow(base, p - 1, prime)) + ord(text[i + p])) % prime
            window_hash = (window_hash + prime) % prime
    return result
