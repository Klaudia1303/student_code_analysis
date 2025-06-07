n=int(input("Inserire un numero dispari intero >2: "))
if n%2==0 or n<3:
    print("Il numero deve essere dispari e maggiore uguale a 3")
else:
    for i in range(n):
        if i==0 or i==n-1:
            print('*'*n)
        else:
            print('*'+' '*(n-2)+'*')
