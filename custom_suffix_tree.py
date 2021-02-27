"""
This suffix tree is an altered version of GeeksforGeeks' Java code.
For reference, see https://www.geeksforgeeks.org/count-distinct-substrings-string-using-suffix-trie/
"""

protein_alphabet = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
protein_alphabet_size = len(protein_alphabet)


class Node(object):
    def __init__(self):
        self.children = list()
        for _ in range(protein_alphabet_size):
            self.children.append(None)

    def insert_suffix(self, suffix: str):
        if len(suffix) > 0:
            c_index: int = protein_alphabet.index(suffix[0])
            if self.children[c_index] is None:
                self.children[c_index] = Node()
            self.children[c_index].insert_suffix(suffix[1:])


class SuffixTree(object):
    def __init__(self, sequence: str):
        self.root = Node()
        self.size = 0
        for i in range(len(sequence)):
            self.root.insert_suffix(sequence[i:])

    def _node_count(self, node):
        if node is None:
            return 0
        count = 0
        for i in range(protein_alphabet_size):
            count = count + self._node_count(node.children[i])
        return count + 1

    def node_count(self):
        return self._node_count(self.root) - 1
