base=int(input('inserisci un numero dispari maggiore o uguale a 3 '))
k=0
s=(base//2)
while base%2!=0 and base>=3 and (base-k)>1:
    for i in range(base+1):
        if i%2!=0 or i==1:
            print(' '*(s)+'*'*(i))
            k+=2
            s-=1
