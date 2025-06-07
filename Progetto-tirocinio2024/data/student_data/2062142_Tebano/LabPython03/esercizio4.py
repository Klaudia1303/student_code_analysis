x=int(input('x='))
y=int(input('y='))
while (x<0 or x>10)or(y<0 or y>10):
    x=int(input('x='))
    y=int(input('y='))
i=0
while i<=10:
    if i!=x and y!=i:
        print(i)
    i=i+1    
