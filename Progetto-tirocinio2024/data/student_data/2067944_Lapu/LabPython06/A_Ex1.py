n1=int(input("inserire un numero intero positivo: "))
n2=int(input("inserire un numero intero positivo: "))
if n1>n2:
    for i in range (2, n1+1):
        if n1 % i== 0 and not n2 % i ==0:
            print (i)
