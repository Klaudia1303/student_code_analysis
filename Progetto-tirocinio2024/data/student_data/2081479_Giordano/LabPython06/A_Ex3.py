for vert in range(0,8):
    for hor in range(0,8):
        first=(vert*hor)//8
        second=(vert*hor)%8
        print(first,end="")
        print(second,end=" ")
    print('')