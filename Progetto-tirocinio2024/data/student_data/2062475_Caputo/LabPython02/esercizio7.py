n1 = int(input("inserire il numero n1: "))
n2 = int(input("inserire il numero n2: "))
n3 = int(input("inserire il numero n3: "))
if (n1 > n2):
    if (n1 > n3):
        if (n2 > n3):
            print (n1,"\n"+ str(n2) + "\n" + str(n3))
        else:
            print (n1, "\n" + str(n3) + "\n" + str(n2))
    else:
        print (n3, "\n" + str(n1) + "\n" + str(n2))
elif (n2 > n3):
    if (n1 > n3):
        print (n2, "\n\b" + str(n1) + "\n" + str(n3))
    else:
        print (n2, "\n" + str(n3) + "\n" + str(n1))
else:
    print (n3, "\n" + str(n2) + "\n" + str(n1))
