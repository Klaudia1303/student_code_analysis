n=str(input("Inserisci un numero: "))
counter=0
while n!=0:
    n=int(input("Inserisci un numero: "))
    if n%3==0:
        counter=counter+n
       
        
print("La somma è: ",counter)
