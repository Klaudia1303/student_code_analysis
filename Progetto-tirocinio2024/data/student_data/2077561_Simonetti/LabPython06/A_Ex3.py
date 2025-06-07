for i in range(1,11):
    for j in range(1,11):
        result=i*j
        octResult=oct(result)
        nOctResult=octResult[2:]
        if len(nOctResult)==1:
            nOctResult='0'+nOctResult
        print(nOctResult,end='\t')
    print()
