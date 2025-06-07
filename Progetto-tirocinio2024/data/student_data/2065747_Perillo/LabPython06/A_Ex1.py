n1=int(input("inserire un intero:"))
n2=int(input("inserire un intero:"))
for i in range(n1,0,-1):
    if n1%i==0:
        if n2%i==0:
            continue
        else:
            print(i)
