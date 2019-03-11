#Entrez For Searching Papers
from Bio import Entrez
Entrez.email = "bguglie@hsph.harvard.edu"
#search for key words and get all papers then store IDs
handle = Entrez.esearch(db = "pubmed", term = "sequence illumina assembly", retmode="xml", retmax = 1000)
record = Entrez.read(handle)
#print(record["Count"])
handle.close()
idlist = record["IdList"]
print(idlist)
#Prep my lists to loop through and search for occurance of particular words
mylist = idlist
words = ['spades', 'abbyss', 'allpaths-lg', 'euler',
        'mira', 'velvet', 'edena', 'sga', 'ssake', 'ray',
        'soap de novo', 'minia', 'silva', 'microsoft']
for word in words:
    woi = 0
    print(word.upper())
    for x in mylist:
        handle = Entrez.efetch(db = "pubmed", id=x, rettype = "full", retmode="xml")
        a = handle.read()
        handle.close()
        a = a.lower()
        woi += a.count(word)
    print(word + ' : '+ str(woi))
