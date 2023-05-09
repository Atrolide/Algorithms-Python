def rabin_karp_duplicate_picture(picture, K):
    # Initialize pattern_hash as 0
    pattern_hash = 0
    # Loop through rows of the first K columns
    for i in range(K):
        # Loop through columns of the last K rows
        for j in range(K):
            # Add the hash value of the current pixel to pattern_hash
            # Hash value is calculated by shifting the pixel value by a position based on its row and column
            pattern_hash |= (picture[i][len(picture[0])-K+j] << ((K-i-1)*K + (K-j-1)))

    # Initialize an empty list to store row hashes
    row_hashes = []
    # Initialize prev_row_hash as 0
    prev_row_hash = 0
    # Loop through rows of the picture
    for row in picture:
        # Initialize row_hash as 0
        row_hash = 0
        # Loop through columns of the last K rows
        for j in range(K):
            # Add the hash value of the current pixel to row_hash
            # Hash value is calculated by shifting the pixel value by a position based on its column
            row_hash |= (row[len(row)-K+j] << (K-j-1))
        # XOR the previous row hash with the current row hash and store the result as the current row hash
        row_hash ^= prev_row_hash
        # Append the current row hash to the list of row hashes
        row_hashes.append(row_hash)
        # Update prev_row_hash by shifting it right by 1 and adding the current row hash shifted left by K-1
        prev_row_hash = (prev_row_hash >> 1) | (row_hash << (K-1))

    # Create a list of the first K rows of the picture, each truncated to the last K columns
    pattern = [row[-K:] for row in picture[:K]]
    # Loop through the row hashes, starting from the first row and ending at the row that is K rows from the bottom
    for i, row_hash in enumerate(row_hashes[:len(picture)-K+1]):
        # If the current row hash ANDed with a mask of K*K 1's is equal to pattern_hash, check if the pattern matches the corresponding pixels in the picture
        if row_hash & ((1 << (K*K)) - 1) == pattern_hash:
            # Loop through the pixels in the pattern and check if they match the corresponding pixels in the picture
            if all(pattern[m][n] == picture[i+m][n+len(picture[0])-K] for m in range(K) for n in range(K)):
                # If the pattern matches, return True
                return True
    # If no matching pattern is found, return False
    return False
