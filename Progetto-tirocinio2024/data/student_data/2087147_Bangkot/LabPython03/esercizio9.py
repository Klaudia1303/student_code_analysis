corretto=False
n=int(input())
i=2
p=[i,n]
if n%2==0:
        print(n,str("non è un numero primo"))
elif n%2!=0:
    while n/i!=1:
        if n/p!=1:
            print(n,str("non è un numero primo"))*1  
        elif n/p==1:
            print(n,str(" è un numero primo"))*1
