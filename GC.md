Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.


FASTA format 
every string in file contains > along with labeling information about the string 
the word after > is the identifier of the sequence and the rest of the line is the description no space between > and identifier

GC-content 
of a strand of nucleic acid is the percentage of nucleotides in the strand that has cytosine or guanine bases

Ideas to solve 
