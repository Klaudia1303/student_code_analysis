s=""
print("/t")
for i in range(1,8):
    for j in range(1,8):
        p = i*j
        while p!=0:
            r=p%8
            p=p//8
            s += str(r)
        print (s[::-1], end="\t")
        s = ""
    print("\n")