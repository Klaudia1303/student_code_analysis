n = int(input('inserisci numeratore n: '))
d = int(input('inserisci denominatore d: '))
if n<d:
    print('propria')
elif n%d==0:
    print('apparente')
elif n>d and not n%d==0:
    print('impropria')
