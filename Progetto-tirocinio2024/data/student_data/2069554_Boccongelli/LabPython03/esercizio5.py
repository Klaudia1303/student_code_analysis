finito = False
while (not finito):
    s = input('Inserisci una stringa: ')
    print(s[0] + s[-1])
    if (s.isalpha() and s.islower()):
        finito = True
