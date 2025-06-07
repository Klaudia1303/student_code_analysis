for i in range (2,11):
    for j in range (i,11):
        x=i*j
        if x<=7:
            valore=x
        else:
            valore=''
            while x>0:
                resto=x%8
                x=int(x-resto)-8
                valore=str(resto)+valore
        print('0'+str(i)+'x'+'0'+str(j)+'='+str(valore))
    print()
