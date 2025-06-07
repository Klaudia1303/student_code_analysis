anni=int(input("Inserire l'età del cane: "))
if anni==0 or anni < 0:
         print("Valore non valido")
else:
    if anni<2 and anni>0:
        anni_u=int(anni*10.5)
        print("L'età del cucciolo in anni umani è: "+str(anni_u))
    else:
        anni_u=int(((anni-2)*4)+21)
        print("L'età del cucciolo in anni umani è: "+str(anni_u))        
