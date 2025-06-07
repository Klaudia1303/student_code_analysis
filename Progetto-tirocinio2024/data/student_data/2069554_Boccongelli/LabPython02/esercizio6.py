n = input('Inserisci il numeratore: ')
d = input('Inserisci il denominatore: ')

if (int(n) < int(d)):
    print('propria')
elif (int(n) % int(d) == 0):
    print('apparente')
else:
    print('impropria')
