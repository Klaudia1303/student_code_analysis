a = False
e = 0
e = int(e)

while not a:
    i = input('Inserisci un numero intero: ')
    if i == '0':
        print('La somma degli interi divisibili per tre è:',e)
        a = True
    elif int(i)%3 == 0:
        e += int(i)
