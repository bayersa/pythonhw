

s = "TTGAGAACTGAAGACCATATGATCCTTCACTTGAGAACTGCCCCCTTTGAGAATTGAGAAAATTAGTTGAGAAGGTTGAGAAACTTGAGAACTTGAGAAGGGGAGTTGAGAAATCCAACGCATTCGCCTTGAGAACAGGGCGGGTTGTGTTGAGAACGTGGTTGAGAATTGAGAAACAAGTATTGAGAAATGGCCTTGAGAAACCTTGAGAAGATTGAGAAATACTGCATTGAGAATTGAGAACTTACGGTTGAGAAATTTGAGAACGTGTTGAGAATTGAGAACTTGAGAACTTGAGAATAATTTGAGAAAATTGAGAATTGAGAAGGCTTGAGAACGTTGAGAAATTGAGAAGAGATCTTTGAGAATTGAGAATTGAGAATTGAGAAATTATTGAGAAAACCGGGAGATTGAGAATATTTGAGAAATCTTGAGAAGTTGAGAAATTTGAGAATTTGAGAACTTGAGAAAGTTGAGAATGAGAGAATTGAGAAGAAGCTTGTAGCTTTGAGAAGTTTGAGAATTTGAGAAATTTGAGAAGTATTTGAGAACTTGAGAAGTTGAGAATGTTGAGAATGAAGTGCTTGAGAAATGTTGAGAATTGAGAATGAACACGGAGTTGAGAATTGAGAATGTTGAGAACCAAAACTTGAGAACTGTTTGAGAATTGAGAAGTTGAGAAATATTGAGAAAACGCTTTGAGAATTGAGAACATTGAGAACTTGAGAATTGAGAACTCGGGCATTGAGAATTTTGAGAATTGAGAATTGAGAAGCGGCTTTGAGAAGGCGGTTGAGAAATGTAGTTGAGAATTGAGAATCTTTGAGAACGTTGAGAACTGTGTTGAGAACTTGAGAATGTTGAGAACTTGAGAATATTTGAGAACCATCACGTTGAGAATCCTTGAGAAATTGAGAATTGAGAACAGTTGAGAACGAGTTTGAGAAAATACTTGAGAATTGAGAAAAGTTCATTGAGAA"
t= "TTGAGAATT"

positions=[]

for i in range(len(s) - len(t) + 1):
    if s[i:i+len(t)] == t:
        positions.append(i + 1)
print(" ".join(map(str, positions)))