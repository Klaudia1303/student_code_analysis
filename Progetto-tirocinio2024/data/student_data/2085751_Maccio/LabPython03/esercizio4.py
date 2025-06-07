x=int(input("Inserire un numero compreso fra 0 e 10:  "))
y=int(input("Inserire un numero compreso fra 0 e 10:  "))
if 0<=x<=10 and 0<=y<=10:
    n=0
    while n<=10:
        if x==n or y==n:
           n=n+1
        else:
            print(n)
            n=n+1
