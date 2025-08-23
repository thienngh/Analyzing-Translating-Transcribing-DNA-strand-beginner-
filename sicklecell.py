import amino_acid

def mutation(protein):

    #True  => HbS (E->V at β-globin position 6; index 6 if Met is included)
    #False => Normal (E at that position)

    target = protein[6]
    if target == "E":
        return False
    if target == "V":
        return True
    return None
#Check the 6th protein on the string of DNA starting from Met(position 0)
