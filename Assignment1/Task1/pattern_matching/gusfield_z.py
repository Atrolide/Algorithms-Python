def z_algorithm(s):
    # Get the length of the input string
    n = len(s)

    # Initialize a list of zeros with length n for the Z-values
    z = [0] * n

    # Initialize the left and right boundaries of a Z-box
    l = r = 0

    # Iterate over the indices of s starting from 1
    for i in range(1, n):
        if i <= r:
            # If i is inside the current Z-box, we can use a previous Z-value
            # to initialize the current Z-value
            z[i] = min(r - i + 1, z[i - l])

        # Expand the Z-box centered at i
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1

        # Update the Z-box boundaries if necessary
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    # Return the list of Z-values
    return z


def gusfield_z_search(pattern, text):
    # Concatenate the pattern, a "#" separator, and the text into a new string
    s = pattern + '#' + text

    # Compute the Z-values of the new string using the z_algorithm function
    z = z_algorithm(s)

    # Find the starting positions in text where pattern appears
    # by finding indices i in the Z-array z where z[i] equals the length of pattern
    # Subtract len(pattern) + 1 (to account for the "#" separator) from i to get the starting position
    occurrences = [i - len(pattern) - 1 for i in range(len(z)) if z[i] == len(pattern)]

    # Return the list of starting positions
    return occurrences
