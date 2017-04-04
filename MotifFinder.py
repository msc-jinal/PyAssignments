sequence=raw_input("Enter your String.")
print "Original String is : ",sequence

l=len(sequence)
print "Length of your sequence is : ",l

motif=raw_input("Enter the Motif.")
print "Desire Motif is: ",motif

print "Total number of motif in equence are : ",sequence.count(motif,0)
temp=0
num=0
while num!=-1:
    num=sequence.find(motif,temp)
    if(num!=-1):
        print "motif present at : ",num," position"
        temp=temp+num+2

