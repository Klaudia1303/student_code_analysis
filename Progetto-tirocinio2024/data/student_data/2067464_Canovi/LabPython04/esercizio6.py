a = input("inserisci un numero intero: ")
a = int(a)
b = input("inserisci un numero intero: ")
b = int(b)
x = 0
m = 0
while x < abs(b):
    m = m + a
    x = x + 1
if b < 0:
    print(-m)
elif b >= 0:
    print(m)
