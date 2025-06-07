x=int(input('inserire un nemero per x tra 0 e 10 '))
y=int(input('inserire un nemero per y tra 0 e 10 '))
a=0
while x>=0 and x<=10 and y>=0 and y<=10 and a>=0 and a<=10:
    if a!=x and a!=y:
        print(a)
    a=a+1
