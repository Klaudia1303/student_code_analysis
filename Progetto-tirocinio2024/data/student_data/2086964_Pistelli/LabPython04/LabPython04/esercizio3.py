a=True
i=0
while a==True:
    b=input('inserire un numero ')
    if b=='*':
        print(i)
        a=False
    elif b.isdecimal()>0:
        ''
    elif b.isdecimal()<=0:
        i=i+int(b)
