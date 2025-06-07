s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
for i in range(len(s1)):
    c=s2.find(s1[i])
    if c==-1:
        print(s1[i], end='')
