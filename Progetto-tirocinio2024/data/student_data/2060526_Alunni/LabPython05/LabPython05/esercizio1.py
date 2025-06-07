x=(input('inserisci una stringa:  '))
y=(input('inserisci una stringa avente la stessa lunghezza della prima:  '))
s=str()
if len(x)==len(y):
    l=0
    for i in (x,y):
        while l!=len(x):
            s=(s+x[l]+y[l])
            l+=1
    print(s)
