for i in range(1,11):
    if i<10:
        print(0,end='')
    print(i,end='\t')
    for s in range(2,11):
         if i==1:
            if s<10:
                print(0,end='')
            print(s,end='\t')
         else:
            k=i*s
            ott=''
            m=2
            while m!=0:
                m=k//8
                r=k%8
                ott=str(r)+ott
                k=m
            if len(ott)==1:
                print(0,end='')
            print(ott,end='\t')
    print()

         





     
