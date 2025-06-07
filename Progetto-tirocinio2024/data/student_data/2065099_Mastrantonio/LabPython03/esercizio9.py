n = int (input ('Inserisci un numero intero :'))
i = 2
while i<n :
    if n%i !=0:
        i=i+1
    else :
        i = n+2
        print ('numero non primo')
if i == n:
    print ('numero primo')
