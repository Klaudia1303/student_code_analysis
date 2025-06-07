n=int(input('Inserisci il numero '))
controllo=False
if((n%2==0 or n==1) and n!=2):
    print('Numero non primo')
elif(n%2!=0 or n==2):
    i=2
    while i<n:
        if (n%i==0 and n!=2):
            print('numero non primo')
            controllo=True
            i=n
        elif(n%i!=0 or n==2):
            i+=1
    if controllo==False:
        print('numero primo')
