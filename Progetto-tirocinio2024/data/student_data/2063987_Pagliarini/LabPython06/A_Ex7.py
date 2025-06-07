s1=input()
s2=input()
m=0
seq=''
mseq=''
for i in range(len(s1)):
    z=i
    for l in range(len(s2)):
        if i==len(s1):
            break
        if s1[i]==s2[l]:
            seq= seq + s2[l]
            i+=1
            if len(seq)>=m:
                m=len(seq)
                mseq=seq
        else:
            seq=''
            if len(mseq)>((len(s1)-1)-i):
               break
    i=z
print(mseq)
        

        
               
