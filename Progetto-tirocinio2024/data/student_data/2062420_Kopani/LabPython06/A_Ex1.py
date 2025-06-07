n1=int(input('Inserire il primo intero: '))
n2=int(input('Inserire il secondo intero: '))
for d in range(n1,0,-1):
    if n2%d==0:
        continue
    if n1%d==0:
        print(d)