cane=float(input("Inserisci età cane espresso in anni umani "))
if(cane<=0):
    print("età non valida")
else:
    if(cane>2):
        cane-=2
        eta=(10.5)*2+4*cane
    else:
        eta=(10.5)*cane
    print(eta)
