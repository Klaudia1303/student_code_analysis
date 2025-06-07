a=20
b=1
count=0
for i in range(1000):
    count=count+1
    if a==b:
        print(count)
        break
    a=a+20
    b=b+i+2
