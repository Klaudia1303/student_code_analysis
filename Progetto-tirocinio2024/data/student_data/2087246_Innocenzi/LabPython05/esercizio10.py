lato=int(input("Inserisci il lato: = "))

for i in range(1, lato + 1):
    for k in range(1, lato + 1):
        if i == 1 or i == lato or k==1 or k==lato or i==k or i+k==lato+1:
            print("*",end="")
        else:
            print(" ",end="")
    print("*")