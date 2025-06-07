s1=input('Inserisci una stringa s1: ')
s2=input('Inserisci una stringa s2: ')
for c in s1:
    if c not in s2:
        print(c,end='')