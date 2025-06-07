a=True
i=0
while a==True:
    b=int(input('inserire un numero '))
    if b==0:
        print(i)
        a=False
    elif b%3==0:
        i=i+b
    elif b%3!=0:
        ''
