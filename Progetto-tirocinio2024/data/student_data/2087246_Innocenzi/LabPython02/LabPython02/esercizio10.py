eta=float(input("Inserisci eta' del cane: "))

if(eta>0 and eta>=2):
    EtaPrimiDueAnni=2*10.5
    EtaDopoDueAnni=(eta-2)*4
    EtaCaneConvertita=EtaDopoDueAnni+EtaPrimiDueAnni
    print("Eta' del cane convertita in eta' umana =", EtaCaneConvertita)

elif(eta>0 and eta<=2):
    if(eta==2):
        EtaPrimiDueAnni=2*10.5
        print("Eta' del cane convertita in eta' umana = ", EtaPrimiDueAnni)
    elif(eta<2):
         print("Eta' del cane convertita in eta' umana = ", 10.5*eta)
else:
    print("Input non valido")