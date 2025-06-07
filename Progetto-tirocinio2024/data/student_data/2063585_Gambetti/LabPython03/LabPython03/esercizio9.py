n=int(input('inserisci un numero intero: '))
i=2
finito=False
while not finito:
    d=n%i
    if d==0 and i<n:
        print('numero non primo')
        finito=True
    elif d!=0 and i>=n:
        print('numero primo')
        finito=True
    i=i+1

       
   




       
       
   



