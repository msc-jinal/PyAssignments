str=raw_input("Enter Your DNA Sequence:\n");
print "Your DNA Sequence is: ",str;
rna=str.replace('t','u')
print "Your RNA Aequence is: ",rna.upper()
reve=str[::-1]

print "Reverse Of String : ",reve.upper()
revcomple=""
for x in range(len(reve)):
    if reve[x]=='a':
        revcomple+='t'
        continue
    if reve[x]=='t':
        revcomple+='a'
        continue
    if reve[x]=='c':
        revcomple+='g'
        continue
    if reve[x]=='g':
        revcomple+='c'
        continue
print "ReverseComplement :",revcomple.upper()
    
