n=int(input('Inserisci un intero positivo maggiore di 1 '))
x=2
while (x<n):
    controllo=False
    if(x%2!=0 or x==2):
        i=2
        while i<x:
            if (x%i==0 and x!=2):
                controllo=True
                i=x
            elif(x%i!=0 or x==2):
                i+=1
        if controllo==False:
            print(x)
    x+=1
