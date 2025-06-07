n=int(input('Inserire un numero intero: '))
while n%5!=0:
    n=int(input('Inserire un numero intero: '))
if n%5==0:
    print(n//5)