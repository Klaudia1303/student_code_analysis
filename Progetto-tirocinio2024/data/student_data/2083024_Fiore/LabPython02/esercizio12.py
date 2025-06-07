temp = int(input("temperatura: "))
scala = input("seleziona la scala di valori tra Celius = C e Fahrenheit = F: ")

if scala.lower() == "c":
    if temp <= 0:
        print("L'acqua a temperatura", temp, "è allo stato solido")
    elif temp >= 100:
        print("L'acqua a temperatura", temp, "è allo stato gassoso")
    else:
        print("L'acqua a temperatura", temp, "è liquida")

elif scala.lower() == "f":
    if temp <= 32:
        print("L'acqua a temperatura", temp, "è allo stato solido")
    elif temp >= 212:
        print("L'acqua a temperatura", temp, "è allo stato gassoso")
    else:
        print("L'acqua a temperatura", temp, "è liquida")

else:
    print("La scala scelta non è compresa tra le scelte contemplate")
