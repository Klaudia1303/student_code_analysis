n= int(input('inserisci un numero'))
a = 1
b = 1
print(a)
while n-1>0:
    n -= 1
    print(b)
    temp = b
    b = a+b
    a = temp
