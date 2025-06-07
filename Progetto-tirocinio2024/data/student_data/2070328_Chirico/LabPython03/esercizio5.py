s = input('Scrivi una stringa = ')

if s != '':
    while s.islower() == False or s.isalpha() == False:
        print(s[:1]+s[-1:])
        s = input('prossima = ')

    if s.islower() == True:
        print(s[:1]+s[-1:])
else:
    print('input non valido')
