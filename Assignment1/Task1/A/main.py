from Task1.pattern_matching import *

# Open the text file and read its contents
with open('IlliadByHomer.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Define the pattern to search for
pattern = "black"

# Search for the pattern using brute force
positions = brute_force_search(pattern, text)

# Output the results
if not positions:
    print("Pattern not found")
else:
    for pos in positions:
        # Count the number of lines up to the position of the pattern
        line_num = text.count('\n', 0, pos) + 1
        print(f"Pattern found on line number {line_num}")

