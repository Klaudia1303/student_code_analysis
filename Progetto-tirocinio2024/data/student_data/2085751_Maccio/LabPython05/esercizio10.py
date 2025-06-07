l=int(input("Inserire il lato magiore uguale a 2:  "))
for i in range(1,l+1):
    for k in range(1,l+1):
        if i==l or i==1:
            print("*",end=" ")
        elif k==l or k==1:
            print("*",end=" ")
        elif k-(l-i)==1 or (k-i)==0:
            print("*",end=" ")
        else:
            print("*",end=" ")
    print()
