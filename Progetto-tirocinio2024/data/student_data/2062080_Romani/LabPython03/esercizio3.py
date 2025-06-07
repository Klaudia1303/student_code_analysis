x=False
while not x:
    n=int(input('Inserire numero intero: '))
    if n%5==0:
        print(n//5)
        x=True
    else:
        n=int(input('Inserire numero intero: '))
