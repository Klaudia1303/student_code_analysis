lato=int(input("Lato maggiore o uguale a 2:"))

for i in range(1,lato+1):
    for j in range(1,lato+1):
        if i == 1 or i==lato:
            print("*",end="")
        elif j == 1 or j == lato:
            print("*",end="")
        elif j - i==0 or j-(lato-i) == 1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
