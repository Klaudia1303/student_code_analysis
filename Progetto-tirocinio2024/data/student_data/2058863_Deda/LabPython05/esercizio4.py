n1=int(input('Inserisci intero n1 '))
n2=int(input('Inserisci intero n2 '))
n=0
if n1>0 and n2>0:
    while n<n2:
        for i in range(1,n1*n2):
            n=n1*i
            if n<n2:
                print(n)
else:print('Almeno un intero inserito è <0!')
