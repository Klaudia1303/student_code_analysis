n=int(input("base triangolo isoscele n dispari>3: "))
spazio=""
x=round(float(n/2))-1
y=n-x-x
while y<=n:
    print(" "*x,end=(""))
    print("*"*y,end=(""))
    print(" "*x)
    x-=1
    y+=2
