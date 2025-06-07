n=int(input('inserisci numeratore: '))
d=int(input('inserisci denominatore: '))
m=n%d
if n>=d:
    if m==0: 
        print('apparente')
    else:
        print('impropria')
else:
    print('propria')
