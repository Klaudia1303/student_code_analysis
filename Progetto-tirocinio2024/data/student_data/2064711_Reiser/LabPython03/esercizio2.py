z= int(input('inserire un numero intero "z" maggiore di 0: '))
n = 1
if z>0:
    while z>=n:
        if z%n==0:
            
            print(str(n))
            n= n+1
        else:
            n= n+1
else:
    print('input non valido')
