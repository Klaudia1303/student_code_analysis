s1=input('inserisci una stringa: ')
s2=input('inserisci un\'altra stringa: ')
for c in s1:
    if not c in s2:
        print (c, end='')
