i=0
n='c'
intero_positivo=0
while n!='*':
    n=input('Inserisci un numero intero (* per terminare): ')
    if n.isdecimal() or n[0]in'+-':
        num=int(n)
        if num>0:
            intero_positivo+=1
print(intero_positivo)

