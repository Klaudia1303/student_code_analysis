
x=range(1,9)
y=range(1,9)
for i in x:
    for j in y:
        prod=i*j    
        a=prod//8
        b=prod%8
        a=str(a)
        b=str(b)
        if a+b!='80':
            print(a+b,end='\t')
        else:
            print('100')
        
        
    print()


