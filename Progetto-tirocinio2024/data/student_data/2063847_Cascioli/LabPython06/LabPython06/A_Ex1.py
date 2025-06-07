n1=0
n2=0
while(n1<=0 or n2<=0):
    n1=int(input("Inserire il primo numero [>0]: "))
    n2=int(input("Inserire il secondo numero [>0]: "))
for i in range(n1,1,-1):
    if(n1%i==0 and n2%i!=0):
        print(i)
        continue
