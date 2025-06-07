n=int(input('inserisci un numero intero: '))
s=int(input('inserisci un numero intero: '))
i=0
somma=0
while i!=abs(s):
    i+=1
    if n=='0' or s=='0':
        print('0')
    elif n>0 and s>0:
        somma=somma+n
    elif n<0 and s>0:
        somma=somma+n
    elif n<0 and s<0:
        somma=somma+abs(n)
    elif n>0 and s<0:
        somma=somma-n
print(somma)
