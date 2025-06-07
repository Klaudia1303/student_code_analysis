v1=0
v2=0
for i in range(1,1001):
    v1+=20
    v2+=i
    if v2>=v1:
        print(i)
        break
    
