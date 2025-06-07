s=int(input("inserisci un anno: "))
if s%400==0:
    print("anno bisestile")
elif s%4==0 and s%100!=0:
    print("anno bisestile")
else:
    print("anno non bisestile")
