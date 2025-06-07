n=int(input('inserire un numero intero: '))
i=1
while i!=0:
    if n%5!=0:
        n=int(input('inserire un numero intero: '))
    else:
        x=n/5
        print(x)
        i-=1
        
