def rabin_karp_search(pat, txt):
    # Initialize constants
    q = 101  # A prime number
    d = 256  # The number of possible characters

    # Initialize variables
    m = len(pat)
    n = len(txt)
    h = pow(d, m-1, q)  # pre-compute pow(d, m-1) % q for efficiency
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    results = []

    # Calculate the hash value of pattern and the first window of text
    for i in range(m):
        p = (d*p + ord(pat[i])) % q
        t = (d*t + ord(txt[i])) % q

    # Slide the pattern over the text one by one
    for i in range(n-m+1):
        # Check if the hash values of the current window of text and pattern match
        if p == t:
            # Check for characters one by one to avoid hash collisions
            if pat == txt[i:i+m]:
                results.append(i)

        # Calculate the hash value for the next window of text
        if i < n-m:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+m])) % q

    return results