anno = int(input("inserisci anno: "))
if anno%400==0 or anno%4==0:
 print(anno,"è un anno bisestile")
else:
    print(anno,"non è un anno bisestile")
