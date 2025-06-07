b= int(input('base dispari triangolo isosciele: '))
s=' '
p='*'
h= (b-1)/2
h= int(h)
x=h
y=1

for i in range(b-h):
    print(s*x,p*y)
    y= y+2
    x= x-1

