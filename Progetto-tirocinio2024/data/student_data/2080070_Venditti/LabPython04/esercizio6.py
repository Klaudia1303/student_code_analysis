x=int(input('inserisci un intero: '))
y=int(input('inserisci un intero: '))
absx=abs(x)
absy=abs(y)
z=1
n=1
risultato=0
while z>0:
    z=absy-n
    risultato+=absx
    n+=1
if (x or y)<0:
    print(-risultato)
else:
    print(risultato)
if (x or y)==0:
    print(0)
if x==1:
    print(y)
elif y==1:
    print(x)
