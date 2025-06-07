anno=int(input("Inserisci un anno: "))

if((anno%4==0 and anno%100!=0) or anno%400==0):
    print("Anno e' bisestile")
else:
    print("Anno non bisestile")