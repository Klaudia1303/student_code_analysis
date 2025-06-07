for i in range(0,8):
    for k in range(0,8):
        valore=i*k
        if valore<8:
            print(i,'*',k,'=',valore,'\t',end='')
        else:
            resto1=int(valore%8)
            quoziente=int(valore/8)
            resto2=int(quoziente%8)
            print(i,'*',k,'=',str(resto2)+str(resto1),'\t',end='')
    print()
    print()
