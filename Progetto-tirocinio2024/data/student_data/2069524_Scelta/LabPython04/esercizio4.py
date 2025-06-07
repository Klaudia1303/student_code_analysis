i=0
n='c'
interi_div=0
while n!=0:
    n=int(input('Inserisci un numero intero (0 per terminare): '))
    if n%3==0:
        interi_div+=1
    i+=1
print(interi_div)
