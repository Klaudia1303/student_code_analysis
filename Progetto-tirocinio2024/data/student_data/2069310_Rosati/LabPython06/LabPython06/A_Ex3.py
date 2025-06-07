for i in range(1,9):
    for j in range(1,9):
        ottale=""
        decimale= j*i
        while decimale!=0:
            ottale+=str(decimale%8)
            decimale//=8
        ottale=ottale[::-1]
        if len(ottale)==1:
            print("0"+ottale,end="\t")
        else:
            print(ottale,end="\t")
    print()
