eta=float(input('Inserisci l\'età del cane '))
if(eta<=2 and eta>0):
    print(eta*10.5)
elif(eta>2):
    etac=(2*10.5+(eta-2)*4)
    print(etac)
