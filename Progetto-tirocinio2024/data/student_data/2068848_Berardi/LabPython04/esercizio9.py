n = int(input("inserisci un numero e calcolerò n numeri di fibonacci: "))
a = 1
b = 1
print(a)
while n-1>0:
    n -= 1
    print(b)
    temp = b
    b = a+b
    a = temp