r=0
p=0
for i in range(1,1001):
    r+=20
    p+=i
    if p>=r:
        print(i)
        break
