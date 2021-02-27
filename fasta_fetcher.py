import os
from urllib.error import HTTPError
import datetime

from Bio import Entrez
from Bio import SeqIO


# To make use of NCBI's E-utilities, NCBI requires you to specify your
# email address with each request.
# In case of excessive usage of the E-utilities, NCBI will attempt to contact
# a user at the email address provided before blocking access to the E-utilities.
email: str = open("email.txt", 'r').read()


# Return FASTA as a Python dictionary { refseq: sequence }
def fetch(refseq):
    Entrez.email = email
    try:
        handle = Entrez.efetch(db="protein", id=refseq, rettype="fasta", retmode="text")
    except HTTPError:
        print("Bad RefSeq number: ", refseq, "\nPlease make sure your RefSeq number is correct.")
        exit(-1)

    fasta_iter = SeqIO.parse(handle, "fasta")
    #fasta_dict = {record.name: record.seq for record in fasta_iter}
    for record in fasta_iter:
        fasta_tuple = (record.name, record.seq)
    handle.close()
    return fasta_tuple
