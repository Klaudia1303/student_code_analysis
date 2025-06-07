n=int(input())
s=True
for i in range(2,n):
    if(n%i==0):
        s=False
        print("numero non primo")
        break
if (s==True):
    print("numero primo")
