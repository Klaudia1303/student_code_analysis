base=int(input("inserire un numero dispari, maggiore o uguale a 3:" ))
s=4
for i in range(1,base+1,+2):
    print(" "*s+("*"*(i)))
    s-=1
