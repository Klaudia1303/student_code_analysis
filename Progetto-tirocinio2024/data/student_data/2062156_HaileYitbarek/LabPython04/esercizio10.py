a=input('inserire stringa: ')
b=input('inserire stringa: ')
c=input('inserire stringa: ')
d=''
if  len(a)+len(b)!=len(c):
    while len(a)+len(b)!=len(c):
        d=input('inserire stringa: ')
        a=b
        b=c
        c=d
    print(a,b,d)
else:
    print(a,b,c)
    
    
