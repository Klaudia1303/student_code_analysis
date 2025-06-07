s=str(input("Inserie una stringa:"))
n=str(input("Inserire un'altra stringa:"))
z=str(input("Inserire un'atlra stringa:"))
lunghezzaStr1=len(s)
lunghezzaStr2=len(n)
lunghezzaStrSuc=len(z)
b=True
while b:
    if lunghezzaStr1+lunghezzaStr2==lunghezzaStrSuc:
        print(s,n,z)
        b=False
    else:
        s=n
        n=z
        lunghezzaStr1=lunghezzaStr2
        lunghezzaStr2=lunghezzaStrSuc
        j=str(input("Inserire un'altra stringa"))
        lunghezzaStrSuc=len(j)
        z=j
    
