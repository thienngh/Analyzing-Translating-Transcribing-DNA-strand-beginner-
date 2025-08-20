import codons
import amino_acid
from Bio.Seq import Seq
import time
import string
import sicklecell

print("Hello, welcome to DNA tracing\nWhat do you want to do today?")
user = input("Transcribe, Translate, or Complement DNA?: ")
user = user.lower()

commands = ["transcribe", "translate", "complement dna"]

while True:
    if user in commands:
        my_DNA = input("Input DNA 3' - 5'")
        my_DNA = codons.clean_dna(my_DNA)
        #using DNA chain and turn it into a sequence for future uses
        my_dna = Seq(my_DNA)
        codons.enoughcodons(my_DNA)
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
        chain = ""
        for i in range(len(protein)):
            if i < len(protein) - 1:
                chain += (protein[i] + ' ')
            else:
                chain += protein[i]
        print("Protein chain:", chain)
        while True:
            ans = input("Do you want to check for sickle cell mutation, Y/N?: ").strip().lower()
            if ans in ["y", "n"]:
                break
            print("Please enter Y or N only!")

        if ans == "y":
            if len(protein) >= 6:
                if sicklecell.mutation(protein):
                    print("You have Sickle Cell Anemia mutation")
                else:
                    print("You do not have Sickle Cell Anemia mutation")
            else:
                print("Not enough protein to check")
        else:
            print("Okay, exiting...")




if user == "complement dna":
    #applying bioPython seq
    print("5'-3' DNA:", my_dna.complement())








