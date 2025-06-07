a = False
e = 0
e = int(e)

while not a:
    i = input('Inserisci un numero intero: ')
    if i == '*':
        print('La somma dei soli interi negativi equivale a:',e)
        a = True
    elif int(i) < 0:
        e += int(i)
    
    
