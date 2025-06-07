n=int(input("Inserisci numero intero "))
i=2
x=0
while i<=n:
    if n%i==0:
        i+=1
        x+=1
    else:
        i+=1
if x>1:
    print("Numero non primo")
else: print("Numero primo")
    
