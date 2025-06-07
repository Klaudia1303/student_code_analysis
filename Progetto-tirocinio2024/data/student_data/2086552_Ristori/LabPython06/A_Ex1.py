n1=int(input("Inserire numero intero maggiore di 0:"))
n2=int(input("Inserire un'altro numero intero maggiore di 0:"))
for i in range(n1+1,2,-1):
    if n1%i==0 and n2%i!=0:
        divisore=i
        print(divisore)
