n=0
s=" "
somma=0
while s!="*":
    s=input("Inserisci un intero: ")
    if s=="*":
        print(somma)
        break
    else:
        s=int(s)
        if s<0:
            somma=somma+s
