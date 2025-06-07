c=0
n1=0
n2=0
ris=1
n=int(input('inserire un numero: '))
while(n<0):
    print ('errore')
    n=int(input('inserire un numero: '))
if (n==0 or n==1):
    print(1)
else:
    while (c<=n):
        ris=ris+n2
        n2=n1
        n1=ris
        c+=1
        print(ris)
        
    
