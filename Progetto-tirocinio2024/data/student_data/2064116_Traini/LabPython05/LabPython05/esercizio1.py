#Scrivere un programma che chiede in input all’utente due stringhe aventi la stessa lunghezza e stampa la 
#stringa composta dai caratteri alternati delle due stringhe. Esempi:
#• inserendo nell’ordine “casa” e “mora”, il programma stampa “cmaosraa”
#• inserendo nell’ordine “pippo” e “pluto”, il programma stampa “ppilpuptoo”
s=input('inserire una stringa: ')
i=input('inserire una stringa: ')
for a in range (len(s)):
    h=s[a]+i[a]
    print(h,end='')

    


