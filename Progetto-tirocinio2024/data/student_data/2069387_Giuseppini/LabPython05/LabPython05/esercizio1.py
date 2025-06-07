#Scrivere un programma che chiede in input all’utente due stringhe aventi la stessa lunghezza e stampa la
#stringa composta dai caratteri alternati delle due stringhe.

s1=input('inserisci la prima stringa: ')
s2=input('inserisci la seconda stringa(di lunghezza uguale): ')
somma=''
if len(s1)==len(s2):
    for i in range(0,len(s1)):
        somma=somma+s1[i]+s2[i]
else:
    somma='le stringe devono essere di lunghezza eguale!'
  
    
print(somma)


