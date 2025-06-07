a=True
i=0
while a==True:
    b=input('inserire un numero ')
    if b=='*':
        print(i)
        a=False
    elif b.isdecimal():
        i=i+1
    elif b[1:].isdecimal() and b[0]=='-':
        ''
        
        
