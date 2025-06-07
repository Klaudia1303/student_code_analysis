n = 4
somma = 0
while n != '*' :
    n =  input ('Inserisci un numero intero :')
    if n!= '*':
        if int(n) < 0 :
            somma = somma +1
print (somma)
