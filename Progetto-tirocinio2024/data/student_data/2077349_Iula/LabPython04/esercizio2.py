n=0
s=" "
somma=0
while s!="*":
    s=input("Inserisci un intero: ")
    if s=="*":
        print(n)
        break
    else:
        s=int(s)
        if s>0:
            n+=1

    
