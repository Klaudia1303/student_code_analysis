n=int(input('inserisci un numero intero positivo'))
d=int(input('inserisci un secondo numero intero positivo'))
p=0
for i in range(1,d):
    if n*i<d:
        p=n*i
        print(p)
