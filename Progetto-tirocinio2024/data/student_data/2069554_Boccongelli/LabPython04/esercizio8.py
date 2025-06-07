count = ''
uc = ''
finito = False
while not finito:
    s = input('Inserisci una stringa: ')
    if (uc == s[0]):
        finito = True
        count = count[:-1]
    else:
        uc = s[-1]
        count += s + ' '
print(count)
