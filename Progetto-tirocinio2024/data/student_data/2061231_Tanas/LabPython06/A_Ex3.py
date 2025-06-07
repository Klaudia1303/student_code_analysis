for y in range(1, 9):
    for x in range(1, 9):
        print('{:02o}x{:02o}={:02o}'.format(y,x,y*x),end='\t')
    print()