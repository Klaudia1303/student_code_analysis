for i in range(1,11):
    print('-------------------')
    ris=''
    d=0
    for j in range(1,11):
        ris=''
        s=i*j
        d=s//8
        ris=ris+str(s%8)
        while d!=0:
            ris=ris+str(d%8)
            d=d//8
        if i==10 and j<10:
            print(str(i),'x','0'+str(j),'=',ris[::-1])
        elif i<10 and j<10:
                print('0'+str(i),'x','0'+str(j),'=',ris[::-1])
        elif i==10 and j==10:
            print(str(i),'x',str(j),'=',ris[::-1])
        elif i<10 and j==10:
            print('0'+str(i),'x',str(j),'=',ris[::-1])
            
            
            
            
