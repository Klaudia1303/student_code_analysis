lato=int(input("Inserire il lato del quadrato: "))
if lato>=3:
    for i in range(lato):
        for x in range(lato):
            if i>0 and i<lato-1 and x>0 and x<lato-1:
                print("  ",end="")
            else:
                print("* ",end="")
        print()