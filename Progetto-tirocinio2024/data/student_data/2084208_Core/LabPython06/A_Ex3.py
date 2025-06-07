for i in range(0,8):
    i=i//8+i%8
    for j in range(0,8):
        j=j//8+j%8
        if i<10:
            print('0'+str(i//8+i%8),'*',end=' ')
        else:
            print(str(i//8+i%8),'*',end=' ')
        if j<10:
            print('0'+str(j//8+j%8),'=',end=' ')
        else:
            print(str(j//8+j%8),'=',end=' ')
        if i*j<10:
            print('0'+str(i*j))
        else:
            print(str(i*j))
    
