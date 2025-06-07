x=int(input('inserisci un primo numero intero incluso nell\'intervallo [0;10]: '))
y=int(input('inserisci un secondo numero intero incluso nell\'intervallo [0;10]: '))

c=0
while c<=10:
    if c==x or c==y:
        c=c+1
    else:
        print(str(c))
        c=c+1
