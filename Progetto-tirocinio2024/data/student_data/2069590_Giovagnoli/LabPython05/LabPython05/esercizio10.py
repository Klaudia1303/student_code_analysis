lato=int(input("Inserire il lato del quadrato: "))
t=lato
if lato>=2:
    for x in range(lato):
        t-=1
        for y in range(lato):
            if x==0 or x==lato-1 or y==0 or y==lato-1:
                print("* ",end="")
            elif x==y or y==x or y==t:
                print("* ",end="")
            else:
                print("  ",end="")
        print()