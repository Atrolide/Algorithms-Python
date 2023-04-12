def rabin_karp_duplicate_picture(picture, K):
    # Calculate the hash value of the pattern
    pattern_hash = 0
    for i in range(K):
        for j in range(K):
            pattern_hash |= (picture[i][len(picture[0])-K+j] << ((K-i-1)*K + (K-j-1)))

    # Calculate the hash value of each row
    row_hashes = []
    prev_row_hash = 0
    for row in picture:
        row_hash = 0
        for j in range(K):
            row_hash |= (row[len(row)-K+j] << (K-j-1))
        row_hash ^= prev_row_hash
        row_hashes.append(row_hash)
        prev_row_hash = (prev_row_hash >> 1) | (row_hash << (K-1))

    # Check for duplicates
    pattern = [row[-K:] for row in picture[:K]]
    for i, row_hash in enumerate(row_hashes[:len(picture)-K+1]):
        if row_hash & ((1 << (K*K)) - 1) == pattern_hash:
            if all(pattern[m][n] == picture[i+m][n+len(picture[0])-K] for m in range(K) for n in range(K)):
                return True
    return False
