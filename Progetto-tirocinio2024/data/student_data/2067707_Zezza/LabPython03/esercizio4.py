x=int(input('numero da 0 a 10: '))
y=int(input('numero da 0 a 10: '))
i=0
if x<11 and y<11:
    while i<11:
        print(i)
        if i+1!=x and i+1!=y:
            i=i+1
        elif i+2!=x and i+2!=y:
            i=i+2
        else:
            i=i+3
