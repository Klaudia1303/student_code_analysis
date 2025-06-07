a=int(input())
b=a//2
while b>=0:
    for _ in range(b):
        print(" ", end="")
    for _ in range(a-b*2):
        print("*", end="")
    for _ in range(b-1):
        print(" ",end="")
    if b!=0:
        print(" ")
    else:
        pass
    b-=1

