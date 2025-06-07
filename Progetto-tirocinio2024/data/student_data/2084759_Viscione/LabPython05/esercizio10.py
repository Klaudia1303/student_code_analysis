lato=int(input("immetti il lato del quadrato: "))
for i in range(1,lato+1):
    if i==1 or i==lato:
        print("*"*lato)
    else:
        for j in range(1,lato+1):
            if j==1 or j==i or j==lato-i+1:
                print("*",end="")
            elif j==lato:
                print("*")
            else:
                print(" ", end="")
