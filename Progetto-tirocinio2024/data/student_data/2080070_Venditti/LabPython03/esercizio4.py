x=int(input('inserisci un intero x: '))
y=int(input('inserisci un intero y: '))
a=0
if x>0 and y<10:
    while a>=0 and a<=10:
        if a!=x and a!=y:
            print(a)
        a+=1
else:
    print('valori errati')
