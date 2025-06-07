numeratore=int(input('Inserire il numeratore '))
denominatore=int(input('Inserire il numeratore '))
if numeratore>=denominatore and numeratore%denominatore==0:
    print('apparente')
if numeratore<denominatore:
    print('propria')
if numeratore>denominatore and numeratore%denominatore!=0:
    print('impropria')
