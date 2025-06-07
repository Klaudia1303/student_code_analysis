n=int(input("Inserire un numero intero: "))
i=1
contatore=True
while contatore:
    i+=1
    if n%i==0:
        if n==i:
           contatore=False 
        else:
            print("numero non primo")
            contatore=False
if n==i:
    print("numero primo")
    
