x = int(input('Inserisci un numero da 0 a 10: '))
while x<0 or x>10:
    print('Numero non valido, riprova')
    x = int(input('Inserisci un numero da 0 a 10: '))
y = int(input('Inserisci un secondo numero da 0 a 10: '))
while y<0 or y>10:
    print('Numero non valido, riprova')
    y = int(input('Inserisci un numero da 0 a 10: '))
c=0
while c <=10:
    if c == x: 
        c+=1
    elif c == y:
        c+=1
    print(c)
    c+=1
