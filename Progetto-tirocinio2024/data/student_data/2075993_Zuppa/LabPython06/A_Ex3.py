for i in range(1,8):
    for j in range(1,8):
        n=i*j
        x=n//8
        y=n-(x*8) 
        print('0'+str(i)+'x'+'0'+str(j)+'=',str(x)+str(y),end='  ')
    print()
