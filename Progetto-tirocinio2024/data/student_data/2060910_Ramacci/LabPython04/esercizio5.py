n=int(input("inserire un numero intero maggiore o uguale a 0: "))
r=0
p=n
while n>0:
    r=n-1
    if r>0:
        p=p*r
    n=n-1
print(p)
