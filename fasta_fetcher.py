import os
from urllib.error import HTTPError

from Bio import Entrez
from Bio import SeqIO
import datetime

# To make use of NCBI's E-utilities, NCBI requires you to specify your
# email address with each request.
# In case of excessive usage of the E-utilities, NCBI will attempt to contact
# a user at the email address provided before blocking access to the E-utilities.
email: str = open("email.txt", 'r').read()


# Return FASTAs as a Python dictionary { refseq: sequence }
# Stored .fasta file name will be the date-time of execution if a file name is not specified
def fetch(refseq_list, file_name=str(datetime.datetime.now())):
    Entrez.email = email

    try:
        os.mkdir('./fasta')
    except FileExistsError:
        pass
    if file_name[-6:] != '.fasta':
        file_name = str(file_name + '.fasta')
    fpath = str('fasta/' + file_name)
    file = open(fpath, 'a')
    file.truncate(0)

    for refseq in refseq_list:
        try:
            handle = Entrez.efetch(db="protein", id=refseq, rettype="fasta", retmode="text")
        except HTTPError:
            print("Bad RefSeq number: ", refseq, "\nPlease make sure your inputs are correct.")
            exit(-1)
        file.writelines(handle.read())
    file.close()

    fasta_iter = SeqIO.parse(fpath, "fasta")
    fasta_dict = {record.name: record.seq for record in fasta_iter}
    handle.close()
    return fasta_dict
