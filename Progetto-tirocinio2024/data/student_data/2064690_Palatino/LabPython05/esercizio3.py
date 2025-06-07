s1=input('inserisci la prima stringa: ')
s2=input('inserici la seconda stringa: ')
for c in s1:
    if c not in s2:
        print(c,end='')
