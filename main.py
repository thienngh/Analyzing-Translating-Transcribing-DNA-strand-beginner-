import codons
import amino_acid
from Bio.Seq import Seq
import time
import string

print("Hello, welcome to DNA tracing\nWhat do you want to do today?")
user = input("Transcribe, Translate, or Complement DNA?: ")
user = user.lower()

commands = ["transcribe", "translate", "complement dna"]

while True:
    if user in commands:
        DNA = input("Input DNA 3' - 5'")
        DNA=DNA.upper()
        DNA=DNA.rstrip()
        #break into list then join to remove the white space if were given any white space in between
        DNA = DNA.replace(" ","")
        #using DNA chain and turn it into a sequence for future uses
        my_dna = Seq(DNA)
        break
    else:
        print("Please input approriate demand")
        user = input("Transcribe, Translate, or Complement DNA?: ")
        continue

if user == "transcribe":
    print("\nTranscribing...")
    time.sleep(1)
    mRNA = codons.RNA(my_dna)
    print("mRNA:", mRNA)

protein = list()

if user == "translate":
    print("\nTranscribing...")
    mRNA = codons.RNA(my_dna)
    time.sleep(1)
    print(mRNA)
    print("\nTranslating...")
    time.sleep(1)
    protein = amino_acid.translation(mRNA)

    chain = ''
    if len(protein) < 1:
        print("No START codon detected, please insert it or have the DNA be in 3' - 5'")
    else:
        for i in range(len(protein)):
            if i < len(protein) - 1:
                chain+= (protein[i]+' ')
            else:
                chain += protein[i]
        print("Protein chain:",chain)

if user == "complement dna":
    #applying bioPython seq
    print("5'-3' DNA:", my_dna.complement())









