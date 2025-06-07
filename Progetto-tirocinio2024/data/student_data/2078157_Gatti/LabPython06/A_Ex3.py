for i in range(1,9):
    for j in range(1,9):
        ott = ''
        dec = j*i
        while dec != 0:
            ott += str(dec%8)
            dec//= 8
        ott = ott[::-1]
        if len(ott) == 1:
            print('0' + ott, end = '\t ')
        else:
            print(ott, end= '\t')
    print()
