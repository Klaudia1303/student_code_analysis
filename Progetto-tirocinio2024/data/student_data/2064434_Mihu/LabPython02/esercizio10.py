eta_cane=int(input("Inserisci l'eta del cane da convertire: "))
var=int(0)

if eta_cane<=0:
    print("input non valido")
if eta_cane==1:
    print("Eta umana: ",10.5, "anni")
if eta_cane==2:
    print("Eta umana: ",11, "anni")
if eta_cane>2:
    var=eta_cane-2
    print("Eta umana: ",var*4+11,"anni")
    
