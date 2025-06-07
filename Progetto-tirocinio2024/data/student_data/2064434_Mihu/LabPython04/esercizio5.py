continua=True
i=1
fattoriale=1
n=int(input("Inserisci un numero: "))
while n>0:
    while continua==True:
        if n>=i:
            fattoriale=fattoriale*i
            i=i+1
            
        else:
            continua=False
            print(fattoriale)
if n==0:
    print(fattoriale)
        
