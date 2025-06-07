a=int(input())
if (a%400==0):
    print("anno bisestile")
elif (a%4==0 and a%100!=0):
    print("anno bisestile")
else:
    print("anno non bisestile")
