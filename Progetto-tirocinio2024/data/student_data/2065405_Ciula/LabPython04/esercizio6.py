m=int(input("Inserisci un numero: "))
n=int(input("Inserisci un numero: "))
i=0
somma=0
p=False
if(m<0):
    p=True
while(i<m):
    somma+=n
    i+=1
if(p==True):
    somma*=(-1)
print(somma)
