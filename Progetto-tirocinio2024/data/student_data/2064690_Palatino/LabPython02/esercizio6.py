n=int(input('inserisci il numeratore: '))
d=int(input('inserisci il denominatore: '))
f=n/d
if n<d:
    print('f è una frazione propria')
elif n%d==0:
    print('f è una frazione apparente')
elif n>d and n%d==1:
    print('f è una fraione impropria')
