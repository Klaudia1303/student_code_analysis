EtàCane=float(input("numero reale positivo: "))
if EtàCane<0:
    print("età non valida")
if EtàCane>0 and EtàCane<2:
    print(EtàCane*10.5)
if EtàCane>=2:
    r=(EtàCane-2)*4
    q=2*10.5
    AnniUmani=(r+q)
    print(AnniUmani)
