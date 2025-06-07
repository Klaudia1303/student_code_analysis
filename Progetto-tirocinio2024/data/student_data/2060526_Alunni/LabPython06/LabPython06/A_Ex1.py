x=int(input('inserisci un numero intero maggiore di 0: '))
y=int(input('inserisci un numero intero maggiore di 0: '))
for i in reversed(range(1,x+1)):
    if  y%i==0:
       continue
    if x%i==0:
        print(i)
       
