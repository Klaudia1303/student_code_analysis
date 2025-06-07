def ott(n):
    y=""
    while n!=0:
        k=n%8
        n=n//8
        y=str(k)+y
    return y
for n in range(1,8):
    for m in range(1,8):
        print(ott(n*m),end="\t")
    print()
