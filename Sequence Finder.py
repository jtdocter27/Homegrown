#!/usr/bin/env python
# coding: utf-8
###--------------------------------------------------------------####
#This is a tiny snipped of code that asks NCBI for a FASTA file of a specific genome. In this case, it's set to E.Coli
#It then turns that into a string, parses the string so my computer doesn't explode. 
#Then, it creates a list of nucleotides to check against the genome. 
#Further work could be done to pull a specific protein sequence from another database and then check it vs. the genome. 
###-----------------------------------------------------------------------------------------------------###
#Initial Imports
import Bio
from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'your-email'
handle = Entrez.efetch(db="nucleotide", id="NC_000913", rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")

ecoli_sequence = str(record.seq)
e_small = ecoli_sequence[0:500]
print('The length of the sequence you are checking is: ', len(e_small), 'The Actual Length is: ', len(ecoli_sequence))

#creates two letter combinations of each nucleotide
def cycle_DNA(cycle = ['A','T','C','G']):
    DNAbases = ['A', 'T', 'C', 'G']
    combined = []
    
    for x in cycle:
        for y in DNAbases:
            combined.append(x + y)
    return combined
list1 = cycle_DNA()
print(list1)

#puts each nucleotide pair into a single string. 
DNA_list = ''.join(list1)
#This was just a check 
DNA_list2 = 'GGCGAT'
#print(DNA_list)

#checks the string against the genome 
if DNA_list2 in e_small: 
    print('The sequence is included. John is delighful')
else:
    print('The sequence is not included. John is delightful')

