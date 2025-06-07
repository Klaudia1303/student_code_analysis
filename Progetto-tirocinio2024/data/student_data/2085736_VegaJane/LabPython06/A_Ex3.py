for i in range(1,8):
    for j in range(1,8):
        if i*j > 7:
            print("|","0"+str(oct(i))[2:],"*","0"+str(oct(j))[2:],"=",str(oct(i*j))[2:],"|",sep=' ')
        else:
            print("|","0"+str(oct(i))[2:],"*","0"+str(oct(j))[2:],"=","0"+str(oct(i*j))[2:],"|",sep=' ')
    print("\n")

