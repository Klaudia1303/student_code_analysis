i = input('inserisci numero :')
somma = 0
while i != '0':
    if i != '0' and int(i) % 3 == 0:
        somma = somma + int(i)
    i = input('inserisci numero :')
print(somma)
        
