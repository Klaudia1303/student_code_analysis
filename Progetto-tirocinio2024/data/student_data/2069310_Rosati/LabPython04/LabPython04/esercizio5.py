n=-5
fattoriale=1
while n<=0:
      n=int(input("Inserisci un numero maggiore di 0: "))
      if n==1 or n==0:
         print("1")
         break
      else:
         while n!=0:
               fattoriale=fattoriale*n
               n=n-1
         print(fattoriale)
         break
