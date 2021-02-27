from custom_suffix_tree import SuffixTree

protein_alphabet = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
protein_alphabet_size = len(protein_alphabet)


# Calculate and return the linguistic complexity of given protein sequence
def calculate(seq):
    try:
        distinct_ss: int = _distinct_substring_count(seq)
    except RecursionError:
        distinct_ss: int = _safe_distinct_substring_count(seq)
    max_ss: int = _max_vocab_size(len(seq))
    #print('[INFO] Number of distinct substrings:', distinct_ss)
    #print('[INFO] Maximum vocabulary size:', max_ss)
    return distinct_ss / max_ss


# Helper method that returns the total number of possible amino-acid substrings for given strand size
def _max_vocab_size(m: int):
    res = 0
    for k in range(1, m + 1):
        res = res + min(protein_alphabet_size ** k, m - k + 1)
    return res


def _distinct_substring_count(sequence: str):
    st = SuffixTree(sequence)
    return st.node_count()


def _safe_distinct_substring_count(seq: str):
    sub_count = 0
    for k in range(len(seq)):
        sub_count = sub_count + _kmers(k, seq)
    return sub_count


def _kmers(k: int, seq: str):
    kmer_set = set()
    for i in range(len(seq) - k + 1):
        kmer_set.add(seq[i:i+k])

    return len(kmer_set)
