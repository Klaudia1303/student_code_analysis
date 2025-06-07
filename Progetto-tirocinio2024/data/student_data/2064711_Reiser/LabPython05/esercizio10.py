l=int(input("inserisci il lato del quadrato(intero <=2):"))
for i in range(l):
    for k in range(l):
        if i==0 or i==l-1:
            print("*",end="")
        elif k==0 or k==l-1:
            print("*",end="")
        elif k==i or k==l-1-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
