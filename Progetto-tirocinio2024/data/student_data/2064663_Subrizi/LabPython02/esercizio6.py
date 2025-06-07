n = int(input('Inserisci il valore del numeratore: '))
d = int(input('Inserisci il valore del denominatore: ' ))

frazione_propria = n<d
frazione_apparente = n%d==0
frazione_impropria = n%d!=0 and n>d

if frazione_propria:
    print('propria')
elif frazione_impropria:
    print('impropria')
else:
    print('apparente')
        
