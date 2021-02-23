protein_alphabet = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
protein_alphabet_size = len(protein_alphabet)


# Calculate and return the linguistic complexity of given protein sequence
def calculate(seq: str):
    len_ = len(seq)
    sub_count = 0
    total = __total_subs(len_)
    for k in range(len_):
        sub_count = sub_count + __kmers(k, seq)
    return sub_count / total


# Helper method that returns the total number of possible amino-acid substrings for given strand size
def __total_subs(size: int):
    res = 0
    for n in range(size):
        res = res + min(protein_alphabet_size ** n, size - n + 1)
    return res


# Helper method that returns the number of observed k-sized unique substrings of seq
def __kmers(k: int, seq: str):
    kmer_set = set()
    for i in range(len(seq) - k + 1):
        kmer_set.add(seq[i:i+k])

    return len(kmer_set)