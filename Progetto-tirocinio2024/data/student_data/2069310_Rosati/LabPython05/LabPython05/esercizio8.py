n=2
cont=0
while n<3 or n%2==0:
      n=int(input("Inserisci un numero dispari maggiore o uguale di 3: "))
for i in range(n):
      if i%2!=0:
         cont+=1
s=" "*cont      
for i in range(n+1):
    if i%2!=0:
       print(s,"*"*i)
       cont=cont-1
       s=" "*cont
