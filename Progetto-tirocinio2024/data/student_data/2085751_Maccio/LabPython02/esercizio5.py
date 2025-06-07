a=int(input("Inserire un anno:   "))
if a%4==0 or a%400==0 and a%100!=0:
    print("L'anno",a,"è un anno bisestile")
else:
    print("L'anno",a,"non è un anno bisestile")
