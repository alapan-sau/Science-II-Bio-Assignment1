# Translate the RNA to Protein
def translate(rna):

    rna = rna.replace("\n","")
    rna = rna.replace("\r","")
    rna = rna.upper()

    ## Define the codons
    rna_codon = {
    "UUU": "Phe",
    "UUC": "Phe",
    "UUA": "Leu",
    "UUG": "Leu",

    "UCU": "Ser",
    "UCC": "Ser",
    "UCA": "Ser",
    "UCG": "Ser",

    "UAU": "Tyr",
    "UAC": "Tyr",
    "UAA": "STOP",
    "UAG": "STOP",

    "UGU": "Cys",
    "UGC": "Cys",
    "UGA": "STOP",
    "UGG": "Trp",

    "CUU": "Leu",
    "CUC": "Leu",
    "CUA": "Leu",
    "CUG": "Leu",

    "CCU": "Pro",
    "CCC": "Pro",
    "CCA": "Pro",
    "CCG": "Pro",

    "CAU": "His",
    "CAC": "His",
    "CAA": "Gln",
    "CAG": "Gln",

    "CGU": "Arg",
    "CGC": "Arg",
    "CGA": "Arg",
    "CGG": "Arg",

    "AUU": "Ile",
    "AUC": "Ile",
    "AUA": "Ile",
    "AUG": "Met",

    "ACU": "Thr",
    "ACC": "Thr",
    "ACA": "Thr",
    "ACG": "Thr",

    "AAU": "Asn",
    "AAC": "Asn",
    "AAA": "Lys",
    "AAG": "Lys",

    "AGU": "Ser",
    "AGC": "Ser",
    "AGA": "Arg",
    "AGG": "Arg",

    "GUU": "Val",
    "GUC": "Val",
    "GUA": "Val",
    "GUG": "Val",

    "GCU": "Ala",
    "GCC": "Ala",
    "GCA": "Ala",
    "GCG": "Ala",

    "GAU": "Asp",
    "GAC": "Asp",
    "GAA": "Glu",
    "GAG": "Glu",

    "GGU": "Gly",
    "GGC": "Gly",
    "GGA": "Gly",
    "GGG": "Gly"
    }


    protein_string = ""
    flag = 0
    for i in range(0, len(rna)-(3+len(rna)%3), 3):
        if rna_codon[rna[i:i+3]] =="Met":
            flag=1

        if flag==1:
            protein_string+=(rna_codon[rna[i:i+3]]+' ')
           
        if rna_codon[rna[i:i+3]] == "STOP" and flag==1:
            break
    if(flag==0):
        return "ERROR: No START codon(AUG) found"
    
    else:
        return protein_string
    

# Transcribe DNA to RNA
def transcribe(dna):

    #format
    dna = dna.replace("\r","")
    dna = dna.replace("\n","")
    dna = dna.upper()
    rna = ""

    # mutate = {
    #     'C':'G',
    #     'G':'C',
    #     'A':'U',
    #     'T':'A'
    # }

    for i in dna:
        if(i == 'T'):
            rna+='U'
        else:
            rna+=i

        # rna+=mutate[i]


    rna = rna.lower()
    # print(rna)
    return rna



###########################################################
sample_dna = """
gtttcattataccagtttagatctatcgacagggcgttgagtgtgtgcttactcacggct
ggcatgtaggtaacagtagtggggaagcgtaacatctgaggcctgactcacatatagagt
gtcgaccaaggggtgaagcatcatacgccatacaggcccctagcgaaacgacctagtcta
aagacacacgagaatgaaacccgtggacttggttacagcgtaataatctggtcagagctg
gtccggcgctggcgatgtaccttacgccactgcaaaccggctttgcagagaacatctggg
tacattcccgtgtcatgtcaaagcaggtgattcccgcgaaaaacaattaacgacgcattt
gctattgacgaagtcctagttctccgaattgagcgggagacatatgatgtcgagactgca
ggaaccgaattatcctgtccgcagatccaatagctcacagaggtaaggggagtgtgatgg
tgccctagggtgtttgaacg
"""

dna = input()
if(dna=='0'):
    dna = sample_dna
rna = transcribe(dna)
print("RNA:", rna)

protein = translate(rna)
print("Protein:", protein)
