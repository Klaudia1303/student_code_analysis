#Scrivere un programma che chiede in input all’utente la base di un
#triangolo isoscele (assumete che sia un intero dispari maggiore o uguale a 3)
#e lo disegna sullo schermo, usando il carattere ‘*’.
#Ad esempio, inserendo l’intero “7” per la base del triangolo,
#il programma produce a schermo il seguente disegno
#   *
#  ***
# *****
#*******
#ottenuto stampando tre spazi ed un ‘*’, a capo due spazi e tre ‘*’,
#a capo uno spazio e cinque ‘*’, a capo sette ‘*’.

base = int(input("Inserire la base del triangolo: "))
if base%2!=0 and base>=3:
    i=1
    while i<=base:
        s = int((base-i)/2)
        print(' '*s,'*'*i,' '*s)
        i+=2
        
        
    
