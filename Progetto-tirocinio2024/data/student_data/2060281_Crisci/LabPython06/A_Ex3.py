for i in range(1,9):
    for j in range(1,9):
        n=i*j
        if n<8:
            print('0'+str(i)+'x0'+str(j)+'=0'+str(n))
        else:
            numero=''
            while not(n<8):
                resto=n%8
                numero=str(resto)+numero
                n=n//8
            numero=str(n)+numero
            print('0'+str(i)+'x0'+str(j)+'='+str(numero))
            
            
