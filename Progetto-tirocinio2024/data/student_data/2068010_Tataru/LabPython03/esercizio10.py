n=int(input())
while(n<=1):
    n=int(input())
print("2")
for i in range(3,n+1):
    con=True
    for j in range (2,i):
        if (i%j==0):
            con=False
            break
    if (con==True):
        print(i)
