n = int(input('Quanti numeri?: ' ))
a,b = 1,1
print(a)
print(b)

for i in range(n):
    c = a+b
    a = b
    b = c
    print(c)

