#Scrivere un programma Python che riceve in ingresso due stringhe s1 e s2 non vuote e cerca e stampa la
#sequenza di caratteri più lunga di s1 presente in s2. Ad esempio, se s1='casaletto' e s2='salerno' il programma
#stampa 'sale'. Usare un doppio ciclo for con un break nel ciclo interno.
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
    #i=z
print(mseq)