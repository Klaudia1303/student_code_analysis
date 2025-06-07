eta=input('inserire l\'età del cane: ')
eta=int(eta)
if(eta>=0):
    if (eta>2):
        ris=float((2*10.5)+((eta-2)*4))
        print(ris)
    else:
        ris=float(eta*10.5)
        print(ris)
else:
    print('valore non valido')
