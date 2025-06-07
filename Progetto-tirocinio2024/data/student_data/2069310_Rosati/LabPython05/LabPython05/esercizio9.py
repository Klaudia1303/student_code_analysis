n=2
cont=0
while n<3 or n%2==0:
      n=int(input("Inserisci un numero dispari maggiore o uguale di 3: "))
      
for i in range(n):
    if i==0 or i==n-1:
       print("*"*n)
    else:
       print("*"," "*(n-4),"*")
