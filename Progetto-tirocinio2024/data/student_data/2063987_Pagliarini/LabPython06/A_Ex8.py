s1=input('inserisci stringa')
s2=input('inserisci stringa')
n=int(input('inserisci n'))
for i in range(len(s1)):
    for k in range(len(s2)):
        if s1[i]==s2[k]:
            c=s1[i]
            if s1.find(c)-s2.find(c)==n or s2.find(c)-s1.find(c)==n:
                print(c,end='')
            
