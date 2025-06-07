n1 = int(input('Insert number n>0: '))
n2 = int(input('insert number n>0: '))
v = n1
while v>1:
    v = v-1
    if n1%v==0:
        if n2%v!=0:
            print(v)
