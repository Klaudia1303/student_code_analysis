i=0
n='c'
intero_negativo=0
while n!='*':
    n=input('Inserisci un numero intero (* per terminare): ')
    if n.isdecimal() or n[0]in'+-':
        num=int(n)
        if num<0:
            intero_negativo+=num
i+=0
print(intero_negativo)

