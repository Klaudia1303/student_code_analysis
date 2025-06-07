n=int(input("Inserisci un numero: "))
i=2
while i<=n/2:
    if n%i==0:
        print("Numero non primo")
        break
    i +=1
if i>n/2:
    print("Numero primo")
      

