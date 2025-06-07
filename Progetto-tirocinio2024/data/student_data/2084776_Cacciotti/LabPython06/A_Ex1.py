n1 = int(input('inserire valore'))
n2 = int(input('inserire valore'))
for i in range (n1,0,-1):
    if n1%i==0 and n2%i!=0:
        print(i)
        
