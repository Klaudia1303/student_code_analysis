print("questo programma, una volta inserito un anno e un mese, stampa il mese successivo\n")
a=int(input("inserire l'anno:"))
m=int(input("inserire il mese:"))
if m<=12 and m>=1:
    
    if m==12:
        m=1
        a+=1
    else:
        m+=1
    print(m,a)
        
else:
    print("input non valido")
