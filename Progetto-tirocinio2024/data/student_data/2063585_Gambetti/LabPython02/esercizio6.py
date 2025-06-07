n=int(input('inserisci un numeratore: '))
d=int(input('inserisci un denominatore: '))
x=int(n)/int(d)
if int(n)<int(d):
    print('la frazione',n,'/',d,'è propria')
elif int(n)>int(d) and round(x)!=x:
    print('la frazione è impropria')
elif int(n)==int(d)or(int(n)>int(d) and round(x)==x):
    print('la frazione è apparente')
