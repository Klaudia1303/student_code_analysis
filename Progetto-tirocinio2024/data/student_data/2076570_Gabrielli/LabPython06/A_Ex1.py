n1=int(input('inserisci numero intero: '))
n2=int(input('inserisci numero intero: '))

i=1
while i>0:
    x=(n1%i==0)
    y=(n2%i==0)
    if (x and not y):
        print(x)

        i=i+1
