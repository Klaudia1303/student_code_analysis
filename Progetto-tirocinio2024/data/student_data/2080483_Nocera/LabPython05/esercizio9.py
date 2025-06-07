lato=int(input("inserisci la lunghezza del lato di un quadrato (maggiore di 3 e dispari) : "))
if lato>=3 and lato%2 !=0:
    spazio=0
    while spazio<(lato/1.7):
        spazio=spazio+1
    print("*"*lato)
    for i in range (lato-2):
        print("*"+" "*(spazio)+"*")
    print("*"*lato)    
else:
    print("il lato scelto è pari oppure è troppo piccolo")
