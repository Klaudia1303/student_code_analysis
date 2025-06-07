n1=int(input("inserire il primo numero intero positivo: "))
n2=int(input("inserire il secondo numero intero positivo: "))
for i in range(n1, n2):
    if i%n1==0:
        print(i)
