x=int(input("inserire un numero: "))
y=int(input("inserire un secono numero: "))
n=-1
if 0<=x<=10 and 0<=y<=10:
    while n<=10:
        n=n+1
        if n!=x and n!=y:
            print(n)
else:
    print("errore")
