n=int(input('scrivi un numero intero maggiore di 0: '))
x=1
while x<=n:
    if n%x==0:
        print(x)
        x+=1
    else:
        x+=1
