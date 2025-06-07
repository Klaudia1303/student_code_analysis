n1=int(input("inserire un numero intero maggiore di 0: "))
n2=int(input("inserire un numero intero maggiore di 0: "))
if n1<0 and n2<0:
    print("input non valido")
r=n1
while r!=1:
    if n1%r==0 and n2%r==0:
        r-=1
    elif n1%r==0 and n2%r!=0:
        print(r)
    r-=1
