var1=int(input("Inserire anno:"))
if var1%4==0 and var1%100!=1 or var1%400==0:
    print("anno bisestile")
else:
    print("anno non bisestile")
