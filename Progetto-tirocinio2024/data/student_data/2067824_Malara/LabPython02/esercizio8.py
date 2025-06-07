a=int(input('lato\t'))
b=int(input('lato\t'))
c=int(input('lato\t'))

if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('equiliatero')
    elif a==b or b==c or a==c:
        print("isoscele")
    else:
        print('scaleno')
