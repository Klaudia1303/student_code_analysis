n=int(input())
a=0


for i in range(1, int((n+1)/2)+1):
    b=int(n-1/2)
    print(" "*b,"*"*(i+a))
    a+=1
    n-=1
