n=int(input())
precedente=0
attuale=1
m=0
risultato=1
while m<n:
    print(risultato)
    risultato=attuale+precedente
    precedente=attuale
    attuale=risultato
    m+=1
