for i in range(1,8):
    print()
    for j in range(1,8):
        v=j*i
        n=(v/8)*10
        c=(v%8)
        n=int(n)
        c=int(c)
        print(n+c,end='\t')

