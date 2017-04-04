x=raw_input("Enter your nucleotide sequence : ").upper()
total=len(x)
a=x.count("A")
t=x.count("T")
g=x.count("G")
c=x.count("C")

gctotal=g+c
gccontent=gctotal/float(total)*100

print "Your DNA Sequence is : ",x 
print "Length is : ",total
print "Total A : ",a
print "Total T : ",t
print "Total G : ",g
print "Total C : ",c
print "GC Content : ",gccontent
