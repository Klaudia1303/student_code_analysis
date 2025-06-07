n1=int(input("Inserire un numero intero maggiore di 0: "))
n2=int(input("Inserire un altro numero intero maggiore di 0: "))
for x in range(n1,0,-1):
    if n1%x==0 and n2%x!=0:
        print(x)