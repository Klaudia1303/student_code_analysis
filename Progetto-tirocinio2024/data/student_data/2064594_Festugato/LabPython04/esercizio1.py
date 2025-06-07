i = 0
stringhe = 0
while i>=0:
    s = input('inserisci una striga: ')
    stringhe += 1
    if s.count('c')>=1 and s.count('a')>=1:
        i = -1
    else:
        i += 1
print(stringhe)
