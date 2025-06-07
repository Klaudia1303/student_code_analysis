#Scrivere un programma che chiede in input all’utente due stringhe
#aventi la stessa lunghezza e stampa la stringa
#composta dai caratteri alternati delle due stringhe. Esempi:
#• inserendo nell’ordine “casa” e “mora”, il programma stampa “cmaosraa”
#• inserendo nell’ordine “pippo” e “pluto”, il programma stampa “ppilpuptoo”

s1 = str(input("Inserire una stringa: "))
s2 = str(input("Inserire un'altra stringa: ")) 
if len(s1)==len(s2): 
    for i in range(len(s1)):
        print(s1[i], end='')
        for j in range(i,i+1): 
            print(s2[j], end='')
else:
    print("Le stringhe non hanno la stessa lunghezza!")

