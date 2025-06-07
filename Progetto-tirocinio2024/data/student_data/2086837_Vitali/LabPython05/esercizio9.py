n=int(input("Inserisci lato del quadrato(dispari >=3): "))
for i in range(n):
    if i==0:
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')
print('*'*n)
