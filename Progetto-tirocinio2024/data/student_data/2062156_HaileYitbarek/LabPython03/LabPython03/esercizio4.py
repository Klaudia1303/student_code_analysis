x=int(input('inserire numero intero compreso tra 0 e 10(inclusi): '))
y=int(input('inserire numero intero compreso tra 0 e 10(inclusi): '))
a=0
while 0<=x<=10 and 0<=y<=10 and a<=10:
    if a!=x and a!=y:
        print(a)
        a=a+1
    else:
        a=a+1
    
