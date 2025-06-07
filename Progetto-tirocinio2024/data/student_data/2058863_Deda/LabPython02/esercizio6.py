n=int(input('Inserisci numeratore '))
d=int(input('Inserisci denominatore '))
x=float(n/d)
multiplo=int(n%d)
if x<1:
    print('Propria')
if multiplo==0:
    print('Apparente')
if x>1 and multiplo!=0:
    print('Impropria')
