x=int(input("Inserisci un numero compreso fra 0 e 10: "))
y=int(input("Inserisci un numero compreso fra 0 e 10: "))
inizio=0
while inizio<=10:
    if inizio!=x and inizio!=y:
        print(inizio,"\n")
        inizio=inizio+1
    else:
        inizio=inizio+1
