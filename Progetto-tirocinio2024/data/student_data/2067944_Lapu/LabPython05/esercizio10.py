lato = int(input("lato: "))
for i in range(lato):
    for j in range(lato):
        if(i==j or (i+j==(lato-1))) or ((i==0)or(j==0)) or ((i==(lato-1)) or (j==(lato-1))):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
