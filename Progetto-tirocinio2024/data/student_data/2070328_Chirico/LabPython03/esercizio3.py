#Trova il primo numero n divisibile per 5

n = int(input('scrivi vari interi = '))

while n%5 != 0:
    n = int(input('ancora = '))

if n%5 == 0:
    print(int(n/5))
