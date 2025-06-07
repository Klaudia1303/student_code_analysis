s = input('inserisci una stringa (contenente \'a\' e \'c\' per terminare): ')
i = 0
while 'a' not in s or 'c' not in s:
    i += 1
    s = input('inserisci una stringa (contenente \'a\' e \'c\' per terminare): ')
print(i + 1)
