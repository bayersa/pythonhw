
s = "GGGCTTAGTCGTATTGTAGGGATTTGTGACGATGGTCTCCATGTAAGAGGCCATATACAGTGTGGGTAAGTGGAGACTTGTGCTTTTTCGGGTATTGGCCCTTGACCTTTCGCTCCGTTTTGCGCGGGTTCCAATCAGACTGATACGGAACGAACTCTTTCGATCGAAGCAGAGTTCGGTTGTATAGAATGCATCCGGGTAGCAAGGCTCCAGTTCGGGACAAATCAGCGACTATAATTAGAGCTCTATCCAGTCCACCCCTCCTGACGCAAGGATTAGCATTCTGAAGAGCAGCTTTCGGAATCAATAGCACTCCCTGCCGGCGGTAACCAATCCATAGACTTTATTTTGGTACTAGATTCTTAGGTGCAAAACAGGCCAAAAAATTATGGACTCTGGGCGGACATCATGGTTGCTAGTAGCTTCCGAAGGAAGACTTCTTGCCGGTACTCGTCTCGCCCGATTGAACCCAGGCACAGGGTCGTTTAAAATCGCAGTGAAACACTGCTATGCCAGAGCACCGACGGTTCATACCTCCATCTCGGACTTCTATGATAGTTCTTCTAACTATGGGCCCTTGTCTCCCGGTATCATCAATAAAGCTTCACGAATCACCCCACGTGGTTTCCGATTCAGTATCATGCCTATAATGTTGCTCATGCGCCGCACCGACATTACTTGACGTGGCCTGCCATGCTATGCTGCGTCAGATTTAGGTTTACGCAGACAGCATGGTTCGCTAGGGCTCTTGTTTATCTCCTTGGACCTAGGATTCCTACGCAATAACCATTAGGTTGTAGCCTACTGGGTTGCACATCAGACTTGCCACGATTCTCACCACGAAGATGGTGACCCCAAGGCTGTTTGTTCAAGTATGATACAGCGAGATGTTATCCCGTCCTATCCGACCTGTGCGTGTCCTTGGATGTGCAGCATTC"
t = "TGCGCTGGTCGCCGTATATTTACACGTGCCAGGACTCTTAAAATTGCAAGCACAATTTGGACTAGTTGAGCGAAAAGTTGTCCTTATTCGAAAAAGAGGACGTAGCCTTACGGAGACTATCTCGCGCGGTATGAGCAGTAGGTTCTGGTTCAACATCCTTCCATTTATCCCGAGGGCGCGTGTATGGAACCAATTAGGGAACCGAGTGAGACTCTAGTTGCTATGCGCCGACTAGAATGAGCCAGCCATCCACAGTACTCCGCGCGGAGCAACGGTTCTACTGATGCAACGTCGCATTGCAACCCAATAGCCTTGTAAGGCGTCGGTTAGCAATTCATAGCAATTTTAACTGAAAGATATTCCGGAGTGTTCAGTAATCCACACCGCGCCGGTCCACGGGCGGATAACATGCCTGCCAGTTCGTTCAGGTCAAACACTGATTGCGTTTGTGCTCCTGGCAGGATTGAACACGGCCACAAGGTCTTTGGACGAGGTATCAAATCCGCGCCACATGTACGTACTAAGGGCTGTTCCGCCAATGGTAAAATTCTCATAAGGTTCGGCCTACTATGGGTTTATTGGAGCTGCTGCGAAACATGCCAAATCGTCACGTTCGCAATGGCGACTATGGGGGACTGGCGCGACTTTATTGTTAAATATAATCCTCAACCAGATTATCAGACCTCGCCTCCGATGTTCCTAACCGGCAAAACGAGGTACACGGTCGCAGCGTGATACTATTTAGATCATGATTATCACTTTGTCTGTAGAAAGCTCACGCTGTCAATATGATATTGTCTTCAAATGGATTCGGAATCATCGGTCATACCATGTGAACCGTGCTCCTGACTGTACCAATGCTTTTTGCGGGAGTATCATACGGGGAGATAAGTTACACTCAAAACGAAGTCAAGAGGCGCTGTGTAATCGCTGGATTG"

hamming_distance = 0 

for base in range(len(s)):
    if s[base] != t[base]:
        hamming_distance += 1
print("Hamming Distance:", hamming_distance)

