n1=int(input('inserire un numero: '))
n2=int(input('inserire il secondo numero; '))
if n1>0 and n2>0:
    for numero in range(n1,0,-1):
        if n1%numero==0 and n2%numero!=0:
            print(numero)
