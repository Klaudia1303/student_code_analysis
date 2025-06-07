y=int(input("Inserisci un anno"))
if y%4==0 and y%100!=0 or y%400==0:
    print("Anno bisestile")
else:
    print("Anno non bisestile")
