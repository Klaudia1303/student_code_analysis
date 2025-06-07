n=input('inserisci il numeratore: ')
n=int(n)
d=input('inserisci il denominatore: ')
d=int(d)
if (n>d):
    print('la frazione è impropria')
else:
    if(d%n==0):
        print('la frazione è apparente')
    else:
        if(n%d==0):
            print('la frazione è apparente')
        else:
                print('la frazione è propria')
