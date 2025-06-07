temperature = float(input("Inserisci temperatura: "))
unit = input("Inserisci unità di misura: ")
F = 'F'
C = 'C'
if unit==C:
    if temperature<=0:
        print("solida")
    elif temperature>=100:
        print("gassosa")
    else:
        print("liquida")
elif unit==F:
    if temperature<=0:
        print("solida")
    elif temperature>=(100*1.8)+32:
        print("gassosa")
    else:
        print("liquida")
else:
    print("input non valido")
    
