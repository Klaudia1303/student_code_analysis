n=int(input('inserisci un numero intero'))
d=int(input('inserisci un numero intero'))
if(n<d):
 print('la frazione è propria')
elif(n%d==0):
 print('la frazione è apparente')
elif(n>d and n%d>0):
 print('la funzione è impropria')
