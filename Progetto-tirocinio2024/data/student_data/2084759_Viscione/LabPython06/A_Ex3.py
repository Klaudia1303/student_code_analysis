for i in range(1,9):
    for j in range(1,9):
        m=i*j
        ott=""
        while m!=0:
            ott=str(m%8)+ott
            m=m//8
        if i*j<=7:
            ott="0"+ott
        if i==8:
            outi="10"
        else:
            outi="0"+str(i)
        if j==8:
            outj="10"
        else:
            outj="0"+str(j)
        print(outi+"x"+outj+"="+ott)
