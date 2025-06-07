s=int(input('inserisci numero intero per verificare se è primo: '))
t=2
boo=True

while t<s:
    if s%t==0:
        boo=False
    t+=1
if boo and s!=1:
    print('numero primo')
else:
    print('numero non primo')
