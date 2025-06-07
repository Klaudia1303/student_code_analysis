#esercizio 7
a = int(input('inserisci un intero: '))
b = int(input('inserisci un secondo intero: '))
c = int(input('inserisci un terzo intero: '))
print(max(a , b, c))
print(max(min(a, b), min(a, c), min(b, c)))
print(min(a, b, c))
