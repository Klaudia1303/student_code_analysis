n=int(input('inserisci un numero maggiore di 2:'))
if n<=2:
    n=int(input('errato, inserisci un numero maggiore di 2:'))
i=2
while i<n-1:
    print(i+2)
    i+=2
