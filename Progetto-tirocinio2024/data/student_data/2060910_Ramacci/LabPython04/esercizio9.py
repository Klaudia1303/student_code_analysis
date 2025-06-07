n=int(input("inserire un numero intero maggiore di 0: "))
r=1
p=1
print(r)
print(p)
for i in range(1,n-1):
    t=r+p
    r=p
    p=t
    print(t)
