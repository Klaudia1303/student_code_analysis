a=int(input('inserire numero intero: '))
b=int(input('inserire numero intero: '))
f=a
h=a
if a==0 or b==0:
    print('prodotto: ',str(0))
elif a==1:
    print('prodotto: ',b)
elif b==1:
    print('prodotto: ',a)
elif a==1 and b==1:
    print('prodotto: ',str(1))
else:
    if a>0 and b<0:       
        c=-1
        while c>=b:
            f=f+a
            d=f-h
            c=c-1
        d=-d
        print('prodotto: ',(d))
    if a<0 and b>0:
        c=1
        while c<=b:
            f=f+a
            d=f-h
            c=c+1
        print('prodotto: ',(d))
    if a<0 and b<0:
        c=-1
        while c>=b:
            f=f+a
            d=f-h
            c=c-1
        d=-d
        print('prodotto: ',(d))
    if a>0 and b>0:
        c=1
        while c<=b:
            f=f+a
            d=f-h
            c=c+1
        print('prodotto: ',(d))
        
        
        

