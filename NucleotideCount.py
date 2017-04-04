seq=raw_input("Enter Your Sequence : ")
print seq
print seq.upper()
l=len(seq)
print "Length of given Sequence is :",l

a=0
g=0
t=0
c=0

for ch in seq:
    if(ch == 'a'):
        a=a+1
    elif(ch == 'g'):
        g=g+1
    elif(ch == 't'):
        t=t+1
    elif(ch == 'c'):
        c=c+1
    else:
        print "There is non Nucleotide character."
        break
else:
    print "Total Number of a : %d\nTotal Number of t : %d\nTotal Number of g : %d\nTotal Number of c : %d" % (a,t,g,c)
