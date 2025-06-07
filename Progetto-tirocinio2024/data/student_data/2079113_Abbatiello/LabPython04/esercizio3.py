i = input('inserisci numero :')
somma = 0
while i != '*':
    if int(i) < 0:
        somma = somma + int(i)
    i = input('inserisci numero :')
print(somma)        
