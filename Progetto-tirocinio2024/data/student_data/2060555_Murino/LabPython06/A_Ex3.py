otto=0
ottale=0
d=0
for i in range (1,8):
    for j in range (1,8):
        d=i*j
        otto=str(d//8)+str(d%8)
        print(str(i)+'*'+str(j) + '='+ otto)
    print()
