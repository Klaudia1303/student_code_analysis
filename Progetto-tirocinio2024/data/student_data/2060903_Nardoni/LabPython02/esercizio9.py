m=int(input("Inserisci un intero che indica il mese"))
a=int(input("Inserisci un intero che indica l'anno"))
if m>=1 and m<=12:
    if m==12:
        m=1
        a+=1
        print(m,a)
    else:
        m+=1
        print(m,a)
else:
    print("Input non valido")
