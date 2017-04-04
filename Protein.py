str=raw_input("Enter your dna sequence:").upper()
print "DNA Sequence: ",str
rev=str[::-1]
print "REVERSE of the Sequence: ",rev
revcom=rev.replace("T","U")
print "Reverce complimentory Sequence: ",revcom
rna=str.replace("T","U")
print "RNA Sequence: ",rna

print "Start and Stop Codon Record.\n"
map = {"AUG":"Start","UAA":"stop","UAG":"stop","UGA":"stop"}

for i in range(0,len(rna),3):
    codon=rna[i:i+3]
    if (codon=="AUG"):
        print codon,"-->",map[codon]
    elif (codon=="UAA"):
        print codon,"-->",map[codon]
    elif (codon=="UAG"):
        print codon,"-->",map[codon]
    elif (codon=="UGA"):
        print codon,"-->",map[codon]

    
    

