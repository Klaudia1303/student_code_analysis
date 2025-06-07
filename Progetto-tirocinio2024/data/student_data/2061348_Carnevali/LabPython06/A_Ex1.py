x=int(input("inserire numero: "))
y=int(input("inserire numero: "))
if (x and y)>0:
    for n in range(x,0,-1):
        if x%n==0 and y%n!=0:
            print(n)
else:
    print("errore")
