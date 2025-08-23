import codons
#find the amino acid fits the inserted RNA sequence
def amino(codons):
    genetic_code = {
        # Phenylalanine & Leucine
        "UUU": "F", "UUC": "F",
        "UUA": "L", "UUG": "L",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",

        # Isoleucine & Methionine (Start)
        "AUU": "I", "AUC": "I", "AUA": "I",
        "AUG": "M",  # Start codon

        # Valine
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",

        # Serine
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "AGU": "S", "AGC": "S",

        # Proline
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",

        # Threonine
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",

        # Alanine
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",

        # Tyrosine & Stop
        "UAU": "Y", "UAC": "Y",
        "UAA": "Stop", "UAG": "Stop",

        # Histidine & Glutamine
        "CAU": "H", "CAC": "H",
        "CAA": "Q", "CAG": "Q",

        # Asparagine & Lysine
        "AAU": "N", "AAC": "N",
        "AAA": "K", "AAG": "K",

        # Aspartic acid & Glutamic acid
        "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",

        # Cysteine, Tryptophan & Stop
        "UGU": "C", "UGC": "C",
        "UGA": "Stop",
        "UGG": "W",

        # Arginine
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AGA": "R", "AGG": "R",

        # Glycine
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
    }
    # I have created a dictionary for such instance
    aa = genetic_code.get(codons,'error')
    return aa

def validate_mrna(mrna):
    if not set(mrna) <= {"A", "U", "C", "G"}:
        raise ValueError("mRNA contains invalid characters (allowed: A,U,C,G)")

def translation(mRNA):
    # let the strand of mRNA to go through, break them down into pair of codon, translate each pair but only start
    # from the AUG codon, before that is stripped off and end at the stop codon
    STOP = ["UAG", "UGA", "UAA"]

    try:
        # validate characters
        if not set(mRNA) <= {"A", "U", "C", "G"}:
            raise ValueError("mRNA contains invalid characters (allowed: A,U,C,G)")
    except ValueError as e:
        print(f"Validation error: {e}")
        return []  # return empty protein if invalid
    
    protein = list()
    started = False
    anti_codons = codons.count_codons(mRNA)

    for aa in anti_codons:
        #aa is the WORD in the list so aa is not like 0 1 2 but rather UAG AUG etc
        if not started:
            if aa == "AUG":
                protein.append(amino(aa))
                started = True #switch started to be true so it will go on to translate the remaining
                continue #finishing the start codon beginining to translate the rest
        if started: #after it's started
            if amino(aa) == "error":
                print("error spotted")
                break  # break if see error
            if aa in STOP:
                break
            protein.append(amino(aa)) # check if its stop then start pasting in the sequence

    return protein

#get the count of each proteins
def count_amino(protein):
    counts = dict()
    for aa in protein:
        counts[aa] = counts.get(aa,0) + 1
    return counts


