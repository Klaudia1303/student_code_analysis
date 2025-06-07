s1=input('inserisci una stringa: ')
s2=input('inserisci una stringa: ')

for c in s1:
    if s2.count(c)==0:
        print(c,end='')
