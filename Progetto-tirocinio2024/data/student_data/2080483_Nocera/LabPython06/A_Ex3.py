for i in range(1,11):
    for j in range(1,11):
        n=i*j
        ottale=""
        while n>0:
            resto=n%8
            n=int((n-resto)/8)
            ottale=str(resto)+ottale
        print(i,"x",j,"=",ottale)
    
