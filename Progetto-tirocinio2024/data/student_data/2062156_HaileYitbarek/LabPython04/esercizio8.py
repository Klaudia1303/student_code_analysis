a=input('inserire stringa: ')
b=input('inserire stringa: ')
c=''
if  a[len(a)-1]!=b[0]:
    while a[len(a)-1]!=b[0]:
        c=input('inserire stringa: ')
        a=b
        b=c
    print(a,c) 
else:
    print(a,b)
        
        
    
