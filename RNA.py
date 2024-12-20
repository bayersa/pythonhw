t = "ATGGGTTCGGTCCGGCTAAGTGAGACGACTAATGGCCATGGTCTGCGTGTTTCGCGTTCTAAGTTATAGGGAGGAACCGTCAGCTAAACCAAGAGGCTACGATCGCCCTAGCCCGCTCCAGCTGTCTAACGTAGACTCAGGTGCGAAATGATGATCTGGAATTTCTTAGCCTTCTTAGCTGAAAAACCTCGGAATACTTACGGTACCATGAATTTTGAGCACGGTCCTTCCGGTCGAGGACTATATATTGGGCCGATTTAAATTTGTAGCGGCCTGAACGAGCGGATCCAATGCTTGTAGTAATTTCTCAGACATTGGCACGTACAAACCGGCTTTTTCGGTATCCCTCCTATGATCAGTAAGCCACAAGAGCGTGTCAAAATCCCACATATTACGTGGTTGGGATAGAGGACTGTCTAATGCGTGGGCCCGTATTCGTCCCCGGTGGGCGTGCGGATTTAGGACACGGGTATGTGCGTAGTAGACAACGCTCTAGTCCAGGGATATACTTGTGACCACGTTCGTCTCTGGCTACACCCGTCCGAAAGTTTATAACTCGCCAAGATATAGAAGCCCGCAACTCCGCCGTGGACGTTTCGCAGGACACACATTAGAGACAAGTGCGGGCCTTAGAGAGATCACCGCTTAGTCTCCCGGGATAGGTAATGAAAGGCGTGTTACCCACTGGATTTCCGAGGTGGTGGACCTTCGTCTCTAGCCCGCCCTGTAACAAATCGGAGAGCGCTCCCTATATGCGATAACCTACGCCCTCCCGTCATCAAGTACTCAGCCGGAGGCCTCCTGATTCCTCAGCCACCACACGTTACATTTTACATGCGTGGCTCCCAAAGTGGACTTTAAGTTCTTGTTTAGTGTAACTGCATGAAGTCGGCTATATGATCAGACCTAAAG"

# Initialize an empty RNA string
u = ""

# Iterate through each character in the DNA string
for nucleotide in t:
    if nucleotide == 'T':
        u += 'U'  # Replace 'T' with 'U'
    else:
        u += nucleotide  # Keep other characters unchanged

# Print the RNA string
print(u)
