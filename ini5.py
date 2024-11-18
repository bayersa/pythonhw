
filepath = "../rosalind_data/ini.txt"

with open(filepath, 'r') as infile:
    lines = infile.readlines()

# Debug the lines read from the file
print("Raw lines:")
print(repr(lines))

# Debug all lines (stripped)
print("\nAll lines (stripped):")
for line in lines:
    print(line.strip())

# Debug sliced lines (even-numbered, 1-based)
print("\nEven-numbered lines (1-based):")
for l in lines[1::2]:
    print(l.strip())
