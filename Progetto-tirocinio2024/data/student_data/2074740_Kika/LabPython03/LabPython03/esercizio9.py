n=int(input('inserisci intero: '))
prec=n
while prec>=2:
    prec=prec-1
    if (n%prec==0) and prec>=2:
        print('numero non primo')
        prec=1
    if (n%prec!=0 and prec==2) or n==2 :
        print('numero primo')
