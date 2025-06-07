n1=int(input("Inserire un intero positivo: "))
n2=int(input("Inserire un altro intero positivo: "))
if n1>0 and n2>0:
    moltiplicazione=0
    i=1
    while moltiplicazione<n2:
        moltiplicazione= n1*i
        i+=1
        if moltiplicazione<n2:
            print(moltiplicazione)
