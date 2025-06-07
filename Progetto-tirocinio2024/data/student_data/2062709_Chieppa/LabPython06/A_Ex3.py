for i in range(0,8):
    for j in range(0,8):
        n=i*j
        q1=n//8
        r=n%8
        resti=str(r)
        if q1==0:
            ottale=r
        else:
            while q1!=0:
                q=q1//8
                r=q1%8
                resti=resti+str(r)
                valore=resti[::-1]
                q1=q
                ottale=int(valore)
        if ottale<10:
            print('0',i,'x','0',j,'=','0',ottale,sep='')
        else:
            print('0',i,'x','0',j,'=',ottale,sep='')
