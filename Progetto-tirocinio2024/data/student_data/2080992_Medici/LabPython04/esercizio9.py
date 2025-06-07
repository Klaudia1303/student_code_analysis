i=0
x=1
y=0
somma=0
n=int(input('inserire un numero intero maggiore di 0: '))
while i<n:
    somma=x+y
    print(somma)
    x=y
    y=somma
    i+=1
    
    
