check=True
n=int(input('inserire numero intero: '))
somma=0
while check and n!=0:
    if n%3==0:
        somma=somma+n
        n=int(input('inserire numero intero: '))
    elif n%3!=0:
        n=int(input('inserire numero intero: '))
    elif n==0:
        break
print(somma)
