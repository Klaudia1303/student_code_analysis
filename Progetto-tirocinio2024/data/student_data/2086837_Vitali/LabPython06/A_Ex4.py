d1=0
d2=0
for i in range(1,1001):
    d1+=20
    d2+=i
    if d2==d1:
        print(i)
        break
