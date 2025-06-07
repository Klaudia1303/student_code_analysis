#eserczio 6
a = int(input('inserisci il numeratore della frazione: '))
b = int(input('inserisci il denominatore della frazione: '))
if a<b:
    print('frazione propria')
elif a>b and a%b !=0:
    print('frazione impropria')
else:
    print('frazione apparente')
