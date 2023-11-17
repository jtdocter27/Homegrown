#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Bio
from Bio import Entrez
from Bio import SeqIO


# In[2]:


Entrez.email = 'jtdocter@gmail.com'
handle = Entrez.efetch(db="nucleotide", id="NC_000913", rettype="fasta", retmode="text")
record = SeqIO.read(handle, "fasta")


# In[3]:


ecoli_sequence = str(record.seq)
e_small = ecoli_sequence[0:500]
len(ecoli_sequence)


# In[4]:


print(e_small)


# In[5]:


def cycle_RNA(cycle = ['A','T','C', 'G']):
    DNAbases = ['A', 'T', 'C', 'G']
    combined = []
    
    for x in cycle:
        for y in DNAbases:
            combined.append(x + y)
    return combined


# In[6]:


list = cycle_RNA()


# In[7]:


RNA_list = ''.join(list)
RNA_list2 = 'GGCGAT'
print(RNA_list)


# In[10]:


if RNA_list2 in e_small: 
    print('The sequence is included. John is delighful')
else:
    print('The sequence is not included. John is delightful')


# In[ ]:




