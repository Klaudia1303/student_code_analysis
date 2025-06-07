for i in range(0, 11):
    for j in range(0, 11):
        print(str(oct(i*j))[2:], end='\t')
        if j == 10:
            print('\n')
