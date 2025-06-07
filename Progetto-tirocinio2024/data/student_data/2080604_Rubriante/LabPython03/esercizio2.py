n=int(input("Inserire in input un numero intero maggiore di 0: "))
n2=1
while n2<n:
    if n%n2==0:
        print(n2)
    n2+=1
