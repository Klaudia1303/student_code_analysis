somma1 = 0
somma2 = 0 
for i in range (1, 1000):
    somma1 = somma1 + 20
    somma2 = somma2 + i
    if ( somma1 == somma2 ):
        break
print ("il numero di giorni necessari al primo viaggiatore per raggiungere il secondo è:", i)
