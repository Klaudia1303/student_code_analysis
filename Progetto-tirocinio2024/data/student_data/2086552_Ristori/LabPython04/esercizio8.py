s=str(input("Inserire la prima stringa:"))
ultimoCaratterePre=s[len(s)-1]
n=str(input("Inserire la seconda stringa:"))
b=True
while b:
    primoCarattereSuc=n[0]
    if ultimoCaratterePre==primoCarattereSuc:
        b=False
        print(j,n)
    else:
         ultimoCaratterePre=n[len(n)-1]
         j=n
         n=str(input("Inserire un'altra stringa:"))
       
        
    
    
