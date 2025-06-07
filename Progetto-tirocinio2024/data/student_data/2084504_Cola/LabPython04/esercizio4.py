n=int(input('inserire un numero intero(0 per terminare): '))
i=0
while n!=0:
    n=int(n)
    if n%3==0:
        i=i+n
    n=int(input('inserire un numero intero(0 per terminare): '))
print(i)
        
    
