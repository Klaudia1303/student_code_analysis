n=int(input('inserisci un numero positivo '))
m=int(input('inserisci un secondo numero positivo '))
p=n
while n>0:
    if p%n==0 and m%n!=0:
        print(n)
    n-=1

    
