n1= int(input())
n2= int(input())


for i in range(1,n2):
    
    r=i*n1
    if r>n2:
        break
    elif r==n2:
        break
    else:
        print(r)
    