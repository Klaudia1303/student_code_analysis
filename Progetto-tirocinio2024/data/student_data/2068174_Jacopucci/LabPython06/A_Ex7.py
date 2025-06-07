s1=input('inserire una stringa non vuota: ')
s2=input('inserire una stringa non vuota: ')
l1=len(s1)
l2=len(s2)
i=0
ris=''
for i in range(l1):
    for i in range(l2):
        if s1[i]==s2[i]:
            ris=str(ris)+str(s[i])
            break
        i+=1
print(ris)
