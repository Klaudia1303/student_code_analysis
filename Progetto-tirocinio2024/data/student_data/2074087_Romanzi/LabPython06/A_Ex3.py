for i in range(1,9):
    for j in range(1,9):
        print(oct(i)[2:],'x',oct(j)[2:],'=',oct(i*j)[2:],sep='')
