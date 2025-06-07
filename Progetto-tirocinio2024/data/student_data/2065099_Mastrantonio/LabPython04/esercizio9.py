n = int (input('Inserisci un numero intero positivo :'))
x1 = 1
x2 = 1
x3 = 0
i= 0
print (x1)
print (x2)
while i<n-2:
    x3 = x2 +x1
    x1 = x2
    x2 = x3
    print(x2)
    i = i + 1
