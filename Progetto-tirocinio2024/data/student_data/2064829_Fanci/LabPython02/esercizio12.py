scala = int(input("premi 1 (temperatura in gradi) o 2(temperatura in fahrenheit): "))
t = float(input("inserisci la temperatura dell'acqua: "))
if scala==2:
    t=(t-32)/1.8
if t>=100:
    print("L'acqua è allo stato gassoso")
elif 0<t<100:
    print("L'acqua è allo stato liquido")
elif t<=0:
    print("L'acqua è allo stato solido")
    
