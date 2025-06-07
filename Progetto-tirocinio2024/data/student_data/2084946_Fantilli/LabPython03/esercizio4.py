x = input()
x = int(x)
y = input()
y = int(y)
i=0
while i<=10:
    if i!=x and i!=(x+1) and i!=y and i!=(y+1):
        print(i)
    elif i==x or i==y:
        print(i+1)
    i+=1
    
