Project Overview

This is my first Python project, where I integrated what I’ve learned into a bioengineering machine learning tool. The program takes a 3'-5' DNA strand as input and generates its complementary 5'-3' DNA strand. From there, it transcribes the sequence into mRNA and then translates it into a protein chain.

The transcription and translation processes are currently powered by dictionaries and custom code I wrote, while BioPython has been integrated to handle complementary DNA strand formation.

At this stage, the tool translates by breaking the sequence into codons and then converting each codon until a STOP codon is encountered. This means it currently works only for DNA sequences that encode a single protein strand. For example, the hemoglobin (Hb) strand can be used to determine the presence of sickle cell anemia. As of right now, it can only be triggered for a translation if "AUG" is spotted. 

Current Features:

-Accepts a DNA strand (3'-5') and produces the complementary strand (5'-3').

-Transcribes DNA into mRNA.

-Translates mRNA into a protein chain.

-Detects sickle cell anemia expression using conditional functions by going through the list of translated proteins and seeing if the one in the 6th position relative to the MET is E or V.



Planned Improvements

-Broader integration of BioPython for sequence analysis.

-Calculation of %C/G content to evaluate DNA stability.

-Implementation of ORF (Open Reading Frame) scanning for more flexible protein prediction.
