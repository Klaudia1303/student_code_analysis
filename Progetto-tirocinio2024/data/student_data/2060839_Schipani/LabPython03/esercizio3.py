n=int(input('inserisci un numero '))
while n%5!=0:
    print(n)
    n=int(input('inserisci un numero '))
    if n%5==0:
        print(int(n/5))
