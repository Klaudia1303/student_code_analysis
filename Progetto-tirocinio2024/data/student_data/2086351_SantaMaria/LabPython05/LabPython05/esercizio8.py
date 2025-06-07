b=int(input('Inserire la base del triangolo isoscele: '))
x=1
while x<=b:
    print(str(' '*int((b-x)/2))+str('*'*x)+str(' '*int((b-x)/2)))
    x+=2
