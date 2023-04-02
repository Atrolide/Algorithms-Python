def rolling_hash(text, start, end, prime):
    p = 31  # prime number for hashing
    hash_value = 0
    power_p = 1

    for i in range(start, end):
        hash_value = (hash_value + (ord(text[i]) - ord('a') + 1) * power_p) % prime
        power_p = (power_p * p) % prime

    return hash_value


def rabin_karp_search(pattern, text):
    prime = 101  # large prime number for hashing
    pattern_hash = rolling_hash(pattern, 0, len(pattern), prime)
    text_hash = rolling_hash(text, 0, len(pattern), prime)

    results = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash and pattern == text[i:i + len(pattern)]:
            results.append(i)

        if i < len(text) - len(pattern):
            text_hash = (text_hash - (ord(text[i]) - ord('a') + 1) * (prime**(len(pattern)-1))) % prime
            text_hash = (text_hash * 31 + (ord(text[i + len(pattern)]) - ord('a') + 1)) % prime
            text_hash = (text_hash + prime) % prime

    return results
