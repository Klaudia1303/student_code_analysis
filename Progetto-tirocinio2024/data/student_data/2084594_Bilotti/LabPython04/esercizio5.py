a = False
e = input('Inserisci un numero intero: ')
e = int(e)
i = 1
o = e * (e * (e - 1))

while not a:
    if e == 0:
        print('Il fattoriale di',e,'è: 1')
    elif e >= 1: 
        print('Il fattoriale di',e,'è:',o)
        a = True
