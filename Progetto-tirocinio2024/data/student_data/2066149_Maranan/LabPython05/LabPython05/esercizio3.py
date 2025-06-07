s1 = input('Inserisci una stringa: ')
s2 = input('Inserisci una stringa: ')
u = ''

for c in s1:
    if c not in s2:
        u = u + c

print (u)
