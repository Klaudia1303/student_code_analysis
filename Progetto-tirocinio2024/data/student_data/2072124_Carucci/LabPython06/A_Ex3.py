for i in range(8):
    for j in range(8):
        p=i*j

        if p<8:
            print(p, end='\t')
            continue
        o=''
        while p>0:
            o += str(p%8)
            p //= 8

        print(o[::-1], end='\t')
    print()
