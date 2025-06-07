c = 0
finito = False
while not finito:
    s = input('Inserisci una stringa (\'c\' e \'a\' per terminare): ')
    c += 1
    if (s.find('c') != -1 and s.find('a') != -1):
       finito = True
       print(c)
