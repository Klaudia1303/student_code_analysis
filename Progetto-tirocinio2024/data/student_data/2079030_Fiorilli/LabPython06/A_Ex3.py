b=''
c=''
for i in range (1,9):
    if i!=8:
        b='0'+str(i)
    else:
        b='10'
    for j in range (1,9):
        if j!=8:
            c='0'+str(j)
        else:
            c='10'
        num=0
        mol=i*j
        a=0
        while mol!=0:
            num+=(mol%8)*10**a
            mol=mol//8
            a+=1      
        if len(str(num))==1:
            num='0'+str(num)
        else:
            num=str(num)
        print(c+'x'+b+'='+num, end='\t')
    print('')

