x=int(input('inserire un numero intero:'))
y=int(input('inserire un numero intero:'))
if x==0 or y==0:
    print('il prodotto vale:',0)
if abs(x)==1:
    print('il prodotto vale:',y)
    if x<0 and y>0 or x>0 and y<0:
        print('il prodotto vale:',-y)
if abs(y)==1:
    print('il prodotto vale:',x)
    if x<0 and y>0 or x>o and y<o:
        print('il prodotto vale:',-x)
risultato=abs(x)
i=1
while abs(y)>i:
    risultato=risultato+abs(x)
    i+=1
if x<0 and y>0 or x>0 and y<0:
    print ('il prodotto vale:',-risultato)
else:
    print('il prodotto vale:',risultato)
