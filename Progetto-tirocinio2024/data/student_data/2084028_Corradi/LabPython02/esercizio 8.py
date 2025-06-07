
    

x=int(input('lato1'))
y=int(input('lato2'))
z=int(input('lato3'))
if x<=0 or y<=0 or z<=0 or x+y<z or x+z<y or y+z<x:
    print('input non valido')
if x==y==z and x>0 or y>0 or z>0 or x+y>z or x+z>y or y+z>x:
    print('equilatero')
if x!=y and x!=z and y!=z and (x>0 or y>0 or z>0 or x+y>z or x+z>y or y+z>x):
    print('scaleno')
    





