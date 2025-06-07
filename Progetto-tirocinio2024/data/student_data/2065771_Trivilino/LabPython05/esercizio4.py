n1=int(input('Inserire un intero positivo: '))
n2=int(input('Inserire un secondo intero positivo: '))
for i in range(1,n2):
    if n1*i<n2:
        print(n1*i)
