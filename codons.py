


def count_codons(codons_string):
    codons_list = list()
    codons_length = 3

    # range ( start, end, step ) so it will print the 3rd letter of every string since step is three AUGUAT => result is A and U
    for codons_start in range(0,len(codons_string),codons_length):
        codons_end = codons_start + 3 #position 3 in 0 1 2
        codons_list.append(codons_string[codons_start:codons_end]) # position end is at 3 but it will only go up to 2
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
