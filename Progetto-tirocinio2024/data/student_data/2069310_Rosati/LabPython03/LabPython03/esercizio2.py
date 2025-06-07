n=0
i=1
while not n>0:
      n=int(input("Inserisci un numero intero maggiore di 0: "))
while not i==n:
      if n%i==0:
         print(i)
      i=i+1
print(n)
