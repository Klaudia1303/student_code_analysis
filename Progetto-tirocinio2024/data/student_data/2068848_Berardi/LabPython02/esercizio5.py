a = int(input("inserisci un anno: "))
if a%400 == 0:
    print("anno bisestile")
else:
    if a%4 == 0:
        if a%100!=0:
            print("anno bisestile")
        else:
            print("anno non bisestile")
    else:
        print("anno non bisestile")