n=int(input('inserisci numeratore: '))
d=int(input('inserisci denumeratore: '))
if n<d:
    print('la frazione è propria')
elif n>d and n%d!=0:
    print('la frazione è impropria')
elif n>d and n%d==0:
    print('la frazione è apprente')
