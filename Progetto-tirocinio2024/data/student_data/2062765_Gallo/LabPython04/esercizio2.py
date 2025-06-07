n=input("Inserisci numero intero: (*per terminare) ")
c=0
while n!="*":
    if int(n)>0:
        c+=1
        n=input("Inserisci numero intero: (*per terminare) ")
    else:
        n=input("Inserisci numero intero: (*per terminare) ")
print(c)

    
