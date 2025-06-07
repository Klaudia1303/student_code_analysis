n1=int(input('Inserire un numero intero>0: '))
n2=int(input('Inserire un numero intero>0: '))
for i in range(n1,0,-1):
    if n1%i==0:
        if n2%i==0:
            continue
        else:
            print(i)
