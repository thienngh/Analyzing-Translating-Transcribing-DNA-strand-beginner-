
from Bio.Seq import Seq

def count_codons(codons_string):
    codons_list = []  # container to hold codons
    codons_length = 3  # codons are 3 bases long

    # range(start, stop, step) → jumps 3 bases at a time
    # len(codons_string) - len(codons_string) % 3 trims off leftover bases
    for codons_start in range(0, len(codons_string) - len(codons_string) % codons_length, codons_length):
        codons_end = codons_start + codons_length  # end index for slice (non-inclusive)
        # slice out exactly 3 characters: seq[0:3] → "ATG"
        codons_list.append(codons_string[codons_start:codons_end])

    return codons_list
def RNA(DNA):
    mRNA =''
    translating_code = {'A' : 'U', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    for nucleotide in DNA:
        rna = translating_code.get(nucleotide,'?')
        mRNA += rna
    return mRNA

def enoughcodons(DNA):
    if len(DNA) % 3 != 0:
        print("There are remaining nucleotides and will be cut at the end")

def clean_dna(s: str) -> str:
    s = s.upper().replace(" ", "").replace("\n", "").replace("\r", "").strip()
    valid = {"A","T","C","G"}
    bad = {ch for ch in s if ch not in valid}
    if bad:
        raise ValueError(f"Invalid DNA symbols: {', '.join(sorted(bad))}")
    return s
def type_strand():
    five_three = False
    while True:
        print("What type is your DNA:")
        ans = input("1 for 3'-5'// 2 for 5'-3': ")
        if not ans in ["1","2"]:
            print("Please insert 1 or 2")
            continue
        else: break
    ans = int(ans)
    if ans == 2: #if 5'-3' detected
        five_three = True
        return five_three
    else:
        return five_three

