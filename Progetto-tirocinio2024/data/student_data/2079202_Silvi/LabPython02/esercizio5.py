print("questo programma verifica se un anno è bisestile\n")
anno=int(input("inserire l'anno:"))
if anno%4==0 and anno%100!=0:
    print("anno bisestile")
else:
    if anno%400==0:
        print("anno bisestile")
    else:
        print("anno non bisestile")
        
