x=int(input('inserisci un numero intero:'))
y=int(input('inserisci un numero intero:'))
i=1
tot=0
if x==0 or y==0:
    print('Il risultato è:',0)

elif (x>0 and y>0) or (x<0 and y>0):
     while i<=y:
         tot+=x
         i+=1
     print('Il risultato è:',tot)

elif x<0 and y<0:
    while i-2>=y:
        tot+=x
        i-=1
    print('Il risultato è:',abs(tot))

elif x>0 and y<0:
    while i<=x:
        tot+=y
        i+=1
    print('Il risultato è:',tot)
    


    

