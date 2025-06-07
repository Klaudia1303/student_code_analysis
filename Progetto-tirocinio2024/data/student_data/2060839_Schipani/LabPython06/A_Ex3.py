def base8(n):
    j=''
    k=1
    while n!=0:
        k=n%8
        j+=str(k)
        n=int(n/8)
    return (str(j)[::-1])
for i in range (1,9):
    print(end='\n')
    for j in range (1,9):
        if len(str(base8(i*j)))==1:
            print('0'+str(base8(i*j)),end='    ')
        else:
            print(base8(i*j),end='    ')
