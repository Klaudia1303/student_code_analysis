for i in range(1,11):
    for j in range(1,11):
        ott=''
        dec=j*i
        while dec!=0:
            ott+=str(dec%8)
            dec//=8
            ott=ott[::-1]
            print(ott, end='\t')
