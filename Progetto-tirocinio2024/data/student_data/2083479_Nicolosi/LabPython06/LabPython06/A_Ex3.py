for i in range(1,11):
    for j in range(1,11):
        x=i*j
        ottale=''
        while x>0:
            resto=x%8
            x=int((x-resto)/8)
            ottale=str(resto)+ottale
        print(ottale,end='\t')
    print()