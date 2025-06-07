b=int(input("immetti base del triangolo: "))
for i in range(1,b+1,2):
    print(" "*int((b-i)/2),"*"*i,sep="")
