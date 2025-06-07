t=input('Inserisci la temperatura e C o F per l\'unità ')
c=t.find('C')
f=t.find('F')
t=t.replace('C','')
t=t.replace('F','')
t=int(t)
if(c!=-1):
    if(t<=0):
        print('solida')
    elif(t>0 and t<100):
         print('liquida')
    elif(t>100):
         print('gassosa')
elif(f!=-1):
    if((t-32)/1.8<=0):
        print('solida')
    elif((t-32)/1.8>0 and (t-32)/1.8<100):
         print('liquida')
    elif((t-32)/1.8>100):
         print('gassosa')
