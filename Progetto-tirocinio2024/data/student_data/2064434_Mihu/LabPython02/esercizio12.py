s=str(input("inserisci la scala che desideri tra 'c' e 'f': "))
t=int(input("inserisci una temperatura: "))
if s=="c":
    if t<=0:
        print("l'acqua è allo stato solido")
    elif t>0 and t<100:
        print("l'acqua è allo stato liquido")
    else:
        print("l'acqua è allo stato gassoso")

if s=="f":
    if t<=32:
        print("l'acqua è allo stato solido")
    elif t>32 and t<212:
        print("l'acqua è allo stato liquido")
    else:
        print("l'acqua è allo stato gassoso")

    
