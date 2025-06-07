for i in range (11):
    for l in range (11):
        p=i*l
        ottP=''
        while p>0:
            ottP=str(p%8)+ottP
            p=p//8
        print (ottP, end=' ')
    print ('\n')
