lato=int(input('inserisci un numero dispari maggiore o uguale a 3 '))
k=0
s=lato-2
while lato%2!=0 and lato>=3 and (lato-k)>1:
    print('*'*lato)
    for i in range(lato+1):
        if i%2!=0 or i==1:
            print('*'+s*' '+'*')
            k+=2
    print('*'*lato)
