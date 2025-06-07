n=int(input('inserisci numeratore: '))
d=int(input('inserisci denominatore: '))
if n%d==0:
    print('apparente')
elif n>d:
    print('impropria')
elif n<d:
    print('propria')
