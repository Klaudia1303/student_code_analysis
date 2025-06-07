numeratore=int(input('numeratore'))
denominatore=int(input('denominatore'))
if(numeratore<denominatore):
    print('propia')
elif(numeratore>=denominatore):
    if(numeratore%denominatore==0):
        print('apparente')
    else:
        print('impropria')
else:
    print('errore')    

