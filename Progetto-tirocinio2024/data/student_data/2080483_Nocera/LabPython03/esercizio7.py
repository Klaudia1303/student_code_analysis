c = str(input("inserisci un carattere :"))
i = 0
while i<2 :
    t = str(input("inserisci una parola :"))
    trovato = t.count(c)
    if  trovato >2:
        i = 4
        
print ("il numero di caratteri trovati è "+str(trovato))

    