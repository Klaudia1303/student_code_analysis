s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')
j=0
for i in range(len(s1)):
    if s1[i] not in s2:
        print(s1[i],end='')
