n1=int(input())
n2=int(input())
for i in range (n1+1,1,-1):
    if n1%(i+1)==0 and n2%(i+1)!=0:
        print(i+1)
        
