n=int(input("Inserire un numero intero dispari: "))
if n%2==0:
    print('Il numero deve essere dispari')
else:
    for i in range(n+1):
        if i%2!=0:
            v=(n-i)/2
            v=int(v)
            print(' '*v+'*'*i)
