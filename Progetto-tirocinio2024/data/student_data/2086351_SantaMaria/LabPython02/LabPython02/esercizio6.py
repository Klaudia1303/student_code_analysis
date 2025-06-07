n=int(input('Inserisci il numeratore: '))
d=int(input('Inserisci il denomoinatore: '))
if n<d:
    print('frazione propria')
elif n%d==0:
    print('frazione apparente')
else:
    n>d and n%d!=0
    print('frazione impropria')
