x=int(input('Inserire il primo numero intero: '))
y=int(input('Inserire il secondo numero intero: '))
i=0
while 0<=i<=10:
    if i!=x and i!=y:
        print(i)
    elif x==y+1 or y==x+1:
        print(i+2)
    elif i==x or i==y:
        print(i+1)
    i += 1