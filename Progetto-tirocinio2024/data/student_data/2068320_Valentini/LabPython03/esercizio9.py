n=int(input("Inserire un numero: "))
i=1
divisori=0
while i<=n:
    resto=n%i
    if resto==0:
        divisori=divisori+1
    i=i+1
if divisori==2:
    print("Numero primo")
else:
    print("Numero non primo")
          
