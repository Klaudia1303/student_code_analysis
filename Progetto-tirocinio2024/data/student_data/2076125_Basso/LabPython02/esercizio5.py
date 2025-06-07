

a=int(input("Inserire anno:\t"))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("Anno bisestile")
        else:
            print("Anno non bisestile")
    else:
        print("Anno bisestile")

else:
    print("Anno non bisestile")
