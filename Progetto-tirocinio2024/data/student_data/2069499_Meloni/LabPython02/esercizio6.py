n=int(input('Inserisci il numeratore '))
d=int(input('Inserisci il denominatore '))
if(n<d):
    print('propria')
elif(n%d==0):
    print('apparente')
elif(n>d and n%d!=0):
    print('impropria')
