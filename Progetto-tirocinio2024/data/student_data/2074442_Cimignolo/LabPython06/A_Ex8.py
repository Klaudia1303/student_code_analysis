s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
n=int(input('inserisci un numero: '))

for c1 in range(len(s1)):
    if s2.count(s1[c1])!=0:
        for c2 in range(len(s2)):
            if s1[c1]==s2[c2]:
                if abs(c1-c2)<=n:
                    print(s1[c1],end='',sep='')
                    break
            
