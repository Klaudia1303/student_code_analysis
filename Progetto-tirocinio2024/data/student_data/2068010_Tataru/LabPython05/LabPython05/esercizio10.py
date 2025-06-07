a=int(input())
b=a-2
for i in range(a):
    if i==0 or i==a-1:
        print("*"*a)
    else:
        for j in range(a):
            if j==0 or j==i or j==a-1-i:
                print("*",end="")
            elif j==a-1:
                print("*")
            else:
                print(" ", end="")

