num=int(input('inserisci un numero maggiore o uguale a 0: '))
i=1
fattoriale=1
if num==0 and num==1:
    print('il suo fattoriale vale 1:')
else:
    while i<=num:
        fattoriale=fattoriale*i
        i=i+1
print('il suo fattoriale vale: ',fattoriale)
