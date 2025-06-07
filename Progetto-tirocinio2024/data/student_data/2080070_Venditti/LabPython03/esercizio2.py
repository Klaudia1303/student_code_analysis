n=int(input("inserisci un numero intero maggiore di 0"))
x=1
if n>0:
    while n>x:
        if n%x==0:
            print(x)
        x+=1
if n<=0:
    print('il valore inserito deve essere maggiore di zero')
