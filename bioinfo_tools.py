'''Bioinfo tool functions'''

import HTSeq
import itertools
import re
import string
import subprocess


def read_fastQ(): 
    '''Reads 200,000 sequences of a fastQ file and writes every sequence to a new file called result.txt'''
    fastq_file=HTSeq.FastqReader("akis.fastq.gz")
    result_f = open("result.txt","w")

    for read in itertools.islice(fastq_file,200000):
        result_f.write(str(read))
    
    result_f.close()
    

 
def gc_content(filename):
    '''Counts the gc bases and returns the percentage of gc 
    content of the whole file'''
    file1 = open(filename,"r")
    gc = 0
    totalBase = 0
    for line in file1:
        line = line.strip("\n")
        if not line.startswith(">"):
            gc += len(re.findall("[GC]", line))
            totalBase += len(re.findall("[GCTA]", line))
    print "GC content per read (/126 bases): ", (gc/200000)
    gc = float(gc) / totalBase
    print "GC content in whole file: ",  (gc * 100)
    
    

    

def read_fasta():
    '''Reads a fasta txt file with
    ids and sequences and creates a 
    dictionary with ID as a key
    and the sequence as an item'''
    try:
        f = open("rosalind_gc.txt")
    except IOError:
        print("File rosalind_gc.txt does not exist")
    seqs={}
    for line in f:
        line=line.strip("\n")
        if line.startswith(">"):
            words=line.replace(">","")
            seqs[words]=''
        else:
            seqs[words]=seqs[words] + line
    print seqs.keys()
    f.close()
    
    
def stop_codon():   
    dna=raw_input("Please enter DNA sequence:")
    stop_codons=["tga","tag","taa"]
    for i in range(0,len(dna),3):
        codon=dna[i:i+3].lower()
        if codon in stop_codons:
            print "Stop codon is found: %s" % codon
            break    

            
if __name__=='__main__':
    read_fasta()
    