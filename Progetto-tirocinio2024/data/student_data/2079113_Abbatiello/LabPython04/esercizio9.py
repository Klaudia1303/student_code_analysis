n = int(input('inserisci numero :'))
a = 1
b = 1
if n < 0 :
    print(errore)
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c)
    
