s=''

for i in range (1,11):
    for j in range (1,11):
        m=i*j
        s=''
        while m>0:
            s=str(m%8)+s
            m=(m-(m%8))//8
        print(s,end=' ')
    print()
            
            
        
        
    print()    
