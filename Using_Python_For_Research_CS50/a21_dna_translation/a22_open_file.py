inputfile = "dna.txt"
f = open(inputfile, "r")
# better way:
# with open(inputfile, "r") as f:
#     seq = f.read()
seq = f.read()

seq = seq.replace("\n", "") # method returns new string, assign that to seq
seq = seq.replace("\r", "") # method returns new string, assign that to seq
# print(seq)

# seq3 = seq.strip() # strips only on end and start line, so does not work here (?)


def translate(seq):
    '''Translate a string containing a nucleotide sequence into a string containing
    corresponding sequence of amino acids. Nucleotides are translated in triplets using 
    the table dictionary.
    '''
    table = { 
            'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
            'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
            'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
            'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
            'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
            'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
            'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
            'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
            'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
            'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
            'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
        } 

    protein = ""
    if len(seq) % 3 == 0:
        for x in range(0, len(seq), 3):
            codon = seq[x : x+3]
            protein+= table[codon]

    return protein

print(translate("ATA"))
print(seq[40:50])
print(help(translate))

def read_seq(inputfile):
    '''
    Reads and returns input sequence with special characters removed.
    '''
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq

prt = read_seq("protein.txt")
dna = read_seq("dna.txt")

print(dna)
print(prt)
print(translate(dna[20:938]))
print(translate(dna[20:935]))

print(prt == translate(dna[20:935]))

print(translate(dna[20:938])[:-1]) # remove last protein element (result of translate)
print(prt == translate(dna[20:938])[:-1])