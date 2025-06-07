a=int(input("Inserisci un numero intero: "))
b=int(input("Inserisci un numero intero: "))
prod=0
if b>0:
   while b>0:
         prod=prod+a
         b=b-1
elif b<0:
   while b<0:
         prod=prod-a
         b=b+1
print(prod)
