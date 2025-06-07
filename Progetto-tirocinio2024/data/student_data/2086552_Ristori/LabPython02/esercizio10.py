var1=str(float(input("Inserire età del cane:")))
parteIntera=int(var1[:var1.find(".")])
dueAnniCane=int(parteIntera-(parteIntera-2))
dueAnniUmano=int(dueAnniCane*10.5)
restoIntAnniCane=int(parteIntera-2)
restoIntAnniUmano=int(restoIntAnniCane*4)
parteDecimale=var1[var1.find(".")+1:]
parteDecimale=float(str("0.")+str(parteDecimale))
if parteIntera==1:
    restoDecimale=float(parteDecimale*10.5)
    print("L'età convertita in anni umani è:",restoDecimale+10.5)
elif parteIntera==0:
    restoDecimale=float(parteDecimale*10.5)
    print("L'età convertita in anni umani è:",restoDecimale)
elif parteIntera>=2:
    restoDecimale=float(parteDecimale*4)
    print("L'età convertita in anni umani è:",dueAnniUmano+restoIntAnniUmano+restoDecimale)











    
    


    
    


    
