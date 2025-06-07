m=int(input("Inserisci un mese "))
a=int(input("Inserisci un anno "))
if((m<=0)or(m>12)):
    print("input non valido")
else:
    m+=1
    if(m>12):
        m=1
        a+=1
        print(m," ",a)
    else:
        print(m," ",a)
