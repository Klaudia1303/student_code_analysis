x=int(input('inserire numero 0<x<10: '))
y=int(input('inserire numero 0<y<10: '))
z=0
if 0<=x<=10 and 0<=y<=10:
    while z<=10:
        if z!=x and z!=y:
            print(z)
            z=z+1
        elif z==x or z==y:
            z=z+1
        
