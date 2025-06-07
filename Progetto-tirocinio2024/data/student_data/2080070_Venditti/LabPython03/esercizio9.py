n=int(input('inserisci un numero intero maggiore di zero: '))
i=1
primo=0
if n>0:
    while n>i:
        if n%i==0:
            primo=primo+1
        i+=1
if n<=0:
    print('il valore inserito deve essere maggiore di zero')
if primo>1:
    print(n,'non è un numero primo')
elif primo==1:
    print(n,'è un numero primo')
