import codons
import amino_acid
from Bio.Seq import Seq
import time
import string
import sicklecell

print("Hello, welcome to DNA tracing\nWhat do you want to do today?")
user = input("Transcribe, Translate, or Complement DNA? or Enter to quit: ")
user = user.lower()
user = user.strip()
while True:
    if user == "":
        print("Thank you!")
        quit()
    commands = ["transcribe", "translate", "complement dna"]

    five_three = False # check if it's 5'-3'
    while True:
        if user in commands:
            my_dna = input("Input DNA: ")
            if my_dna == "":
                quit()
            try:
                my_dna = codons.clean_dna(my_dna)
            except ValueError as e:
                print(e)
                continue

            my_dna = Seq(my_dna)  #using DNA chain and turn it into a sequence for future uses
            if codons.type_strand(): #if it is a 5'-3' we find its complement template strand 3'-5' and perform like normal
                my_dna = my_dna.complement()
                five_three = True
            codons.enoughcodons(my_dna)
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
            print("No START codon detected, please insert it")
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
                        if result is True:
                            print("Mutation detected: Sickle-cell (E→V)")
                        elif result is False:
                            print("Normal hemoglobin")
                else:
                    print("Sequence too short or ambiguous to check")

    if user == "complement dna":
        if five_three: #if it's 5'-3' we already switched to 3'-5' so we need to print the one we already complemented
            print("3'-5' DNA:", my_dna)
        else:
            print("5'-3' DNA:", my_dna.complement())
    user = input("Transcribe, Translate, or Complement DNA? or Enter to quit: ")
    user = user.lower()
    user = user.strip()







