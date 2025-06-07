cont=0
i=0
n=int(input("Inserisci un numero intero: "))
while not i > n:
         i=i+1
         if n%i==0:
            cont=cont+1
if cont==2:
   print("numero primo")
else:
   print("numero non primo")
      
