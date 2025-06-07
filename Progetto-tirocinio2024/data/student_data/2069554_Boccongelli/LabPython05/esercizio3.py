s1 = input('Inserisci una stringa: ')
s2 = input('Inserisci una stringa: ')

for c in s1:
    if (s2.count(c) == 0):
        print(c, end='')
