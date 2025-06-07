s = input ("inserire una stringa alfanumericarica: ")
somma = 0
massimo = 0
carattere = 0
for i in s:
    for j in s:
        if ( i == j ):
            somma = somma +1
    if ( somma >= massimo ):
        massimo = somma
        carattere = i
    somma = 0
print ("il carattere con il numero massimo di ierazioni è:", carattere, massimo)
    
