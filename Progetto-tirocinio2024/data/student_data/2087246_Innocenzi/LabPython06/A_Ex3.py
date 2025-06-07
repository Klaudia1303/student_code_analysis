for i in range(1, 8) :
    for j in range (1, 8) :
        n=i*j
        resto=""
        while(n!=0):
            resto+=str(n%8)
            n//=8
            s1=resto[::-1]
        if len(s1)==1:
            print('0'+s1, end=" ")
        else:
            print(s1, end=" ")
    print("\n")