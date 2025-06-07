print("questo programma converte l'età di un cane, in età umana\n")
aCane=float(input("inserire l'età del cane:"))
aUomo=0
i=2

if aCane>0:
    
    while i>0:
        if aCane>=1:
            aUomo+=10.5
            aCane-=1
            i-=1
            if aCane==0:
                i=0
        else:
            aUomo+=aCane*10.5
            aCane-=1
            i=0

        if aCane>0:
            aUomo+=aCane*4

    print(aUomo)

else:
    print("input non valido")
