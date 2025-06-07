l=int(input("immeti lato quarato: "))
for i in range(1,l+1):
    if i==1 or i==l:
        print("*"*l)
    else:
        print("*"," "*int(l-2),"*",sep="")
