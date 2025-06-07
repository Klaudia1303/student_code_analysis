x=int(input("Inserisci un anno: "))
if (x%400==0) or (x%4==0 and not x%100==0):
    print("Anno bisestile")
else:
    print("Anno non bisestile")