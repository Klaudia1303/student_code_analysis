x = input()
x = int(x)
while x%5 != 0:
    x = input()
    x = int(x)
    if x%5 == 0:
        print(x,'è multiplo di 5, e il loro rapporto equivale a:',x//5)
