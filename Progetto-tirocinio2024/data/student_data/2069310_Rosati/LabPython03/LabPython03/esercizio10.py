n=-1
cont=0
i=0
x=0
while n<1:
      n=int(input("Inserisci un numero intero positivo e maggiore di 1: "))
while i <= n+1:
      if i>=2:
         while x <= i+1:
             if x!=0:
                if i%x==0:
                   cont=cont+1
             x=x+1
         if cont==2:
            print(i)
      cont=0
      x=0
      i=i+1
