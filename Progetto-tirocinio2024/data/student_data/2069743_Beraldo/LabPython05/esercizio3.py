s1=input('inserisci una stringa')
s2=input('inserisci una stringa')
for c in range(len(s1)):
    if s2.find(s1[c]):
        while s2.find(s1[c])==-1:
            print(s1[c],sep='',end='')
            break
