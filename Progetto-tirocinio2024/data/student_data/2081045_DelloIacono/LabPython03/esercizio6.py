c=str(input('inserire una stringha: '))
x=len(c)
i=0
while(i<x and int(ord(c[i])<=100)):
    i=i+1
if(i==x):
      print('stringa consumata e carattere non trovato')
else:
    print('il primo carattere con codice Unicode maggiore di 100 è: '+c[i])
       
