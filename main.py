import codons
import amino_acid

print("hello hello, welcome to DNA tracing")
DNA = input("input a string of DNA: ")
#make the inputed function to look like a 3'-5' DNA strand
DNA = DNA.upper()
#remove ALL the white spaces
DNA = "".join(DNA.split())
print("3'-5' DNA strand =", DNA)

#translate this into a 5'-3' mRNA strand
mRNA = codons.RNA(DNA)
print("5'-3' mRNA strand =", mRNA)

protein = amino_acid.translation(mRNA)

print(protein)

amino_acid.pr1nt_a(protein)


