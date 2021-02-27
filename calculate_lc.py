import os
from sys import argv

import protein_lc
import fasta_fetcher
import plotter


def main():
    refseq: str = str(argv[1])
    fasta = fasta_fetcher.fetch(refseq)
    refseq = fasta[0]
    seq_: str = fasta[1]
    print("[INFO] RefSeq number:", refseq)
    print("[INFO] Sequence size:", len(seq_), "amino-acids.")
    if '-w' in argv:
        window_size_: int = int(argv[argv.index('-w') + 1])
        res: list = slide(seq_, window_size=window_size_)
        plotter.comp_dist(res)
    else:
        res: float = total(seq_)
        print("Linguistic complexity of", refseq, ":", res)


# Second main method I used to generate plots for the report.
def plot_demo_main():
    ws1 = 15
    ws2 = 25
    ws3 = 50
    refseq: str = str(argv[1])
    fasta = fasta_fetcher.fetch(refseq)
    refseq = fasta[0]
    seq_: str = fasta[1]
    #print(seq_)
    print("[INFO] RefSeq number:", refseq)
    print("[INFO] Sequence size:", len(seq_), "amino-acids.")
    print("[INFO] Window sizes:", ws1, ws2, ws3)
    ws1_res = slide(seq_, window_size=ws1)
    ws2_res = slide(seq_, window_size=ws2)
    ws3_res = slide(seq_, window_size=ws3)
    plotter.triple(ws1_res, ws2_res, ws3_res, ws1, ws2, ws3)


def slide(seq: str, window_size: int):
    res: list = list()
    for i in range(0, len(seq)):
        if window_size > len(seq) - i:
            window = seq[i:]
            break
        else:
            window = seq[i:i + window_size]
        res.append(protein_lc.calculate(window))
    return res


def total(seq: str):
    comp = protein_lc.calculate(seq)
    return comp


if __name__ == '__main__':
    main()
    #plot_demo_main()
