x=0
g=0
for g in range(1,10000) :
    x=x+g
    y=20*g
    if x==y:
        print(g)
        break
