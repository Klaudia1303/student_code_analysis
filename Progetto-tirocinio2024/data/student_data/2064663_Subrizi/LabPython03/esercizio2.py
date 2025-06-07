n = int(input(  'inserisci un numero intero maggiore di zero: '))
x=1
while x<=n:
    if n%x==0 and n>0:
        print(x)
    x += 1
