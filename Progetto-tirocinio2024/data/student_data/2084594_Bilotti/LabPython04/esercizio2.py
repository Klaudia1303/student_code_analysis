a = False
e = 0

while not a:
    i = input('Inserisci un numero intero: ')
    if i == '*':
        print('Hai inserito:',e,'numeri interi')
        a = True
    elif int(i) > 0:
        e += 1

