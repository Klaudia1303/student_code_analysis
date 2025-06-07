a=int(input())
b=a-2
for i in range(a):
    if i==0 or i==a-1:
        print("*"*a)
    else:
        print("*",end="")
        for _ in range(b):
            print(" ", end="")
        print("*")
