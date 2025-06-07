side=int(input('insert number: '))
for counter in range(1,side+1):
    if (counter==1 or counter==side):
        print('*'*side)
    else:
        print('*'+' '*(side-2)+"*")