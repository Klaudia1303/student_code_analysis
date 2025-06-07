n= int(input('numero int. n>0: '))
stop= 0
a=0
y=1
x=0

while stop < n:
    x=y
    y=a
    a= x+y
    print(a)
    stop= stop+1

