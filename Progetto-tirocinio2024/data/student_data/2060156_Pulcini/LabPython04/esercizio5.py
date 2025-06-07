n=int(input('inserire un intero >=0:'))
i=n
risultato=1
if n>0:
    if n==0 and n==1:
        print('1')

    while i>0:
        risultato*=i
        i-=1
print(risultato)
