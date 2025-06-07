n = int(input('scrivere un numeratore: '))
d = int(input('scrivere un denominatore: '))
if n<d:
    print('la frazione è propria!')
elif n%d==0:
    print('la frazione è apparente!')
elif n>d and n%d!=0:
    print('la frazione è impropria!')
