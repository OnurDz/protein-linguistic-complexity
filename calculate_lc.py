import os

import protein_lc
import fasta_fetcher
from sys import argv


def main():
    if '-f' in argv and '-p' in argv:
        print("-f and -p should not be used at the same time even though it works.\n"
              "Please consider either entering the name of a file containing RefSeq list following -f "
              "or enter a single RefSeq number following -p\n"
              "Duplicates are eliminated by default.")

    refseq_list = []

    if '-f' in argv:
        try:
            refseq_file = open(argv[argv.index('-f') + 1], 'r')
        except FileNotFoundError:
            print("Specified RefSeq file is not found. Please check your input.\nExiting.")
            exit(-1)

        for line in refseq_file.readlines():
            if line.strip() not in refseq_list:
                refseq_list.append(line.strip())

        refseq_file.close()

    if '-p' in argv:
        refseq_list.append(argv[argv.index('-p') + 1])

    if '--fasta-file' in argv:
        file_name_ = argv[argv.index('--fasta-file') + 1]
        fasta = fasta_fetcher.fetch(refseq_list, file_name=file_name_)
    else:
        fasta = fasta_fetcher.fetch(refseq_list)

    lc_list = []
    result = ""
    for refseq in refseq_list:
        lc_list.append(protein_lc.calculate(fasta[refseq]))
    for i in range(len(lc_list)):
        result = result + (str(refseq_list[i]) + " : " + str(lc_list[i]) + '\n')

    if '--output-file' in argv:
        try:
            os.mkdir("./results")
        except FileExistsError:
            pass

        try:
            output_file = open(str("results/" + argv[argv.index('--output-file') + 1]), 'w')
            output_file.write(result)
        except FileNotFoundError:
            print("Specified output file is not found. Please check your input.\nExiting.")
            pass

    print(result)


if __name__ == '__main__':
    main()
