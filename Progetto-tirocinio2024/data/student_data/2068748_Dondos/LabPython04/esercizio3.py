s=input('Inserisci un numero intero ("*" per terminare): ')
somma_negativi=0

while s!="*":
    n=int(s)
    if n<0:
        somma_negativi+=n
    s=input('Inserisci un numero intero ("*" per terminare): ')
print(somma_negativi)
