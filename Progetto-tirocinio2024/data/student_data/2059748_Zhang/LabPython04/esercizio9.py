i=0
n=int(input("scrivi un intero: "))
x=1
y=1
z=0

if n>0:
    if n==1:
        print(x)
        print(y)
    else:
        print(x)
        print(y)
        while i!=n-2:
            z=x+y
            print(z)
            y=x
            x=z
            z=0
            i+=1
else:
    print("intero >0")
