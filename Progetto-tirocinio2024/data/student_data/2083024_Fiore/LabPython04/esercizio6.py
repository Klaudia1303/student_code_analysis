num1 = int(input("inserisci il prino fattore: "))
num2 = int(input("inserisci il secondo fattore: "))
n = 1
if num1 < 0 and num2 < 0:
    num1 = -(num1)
    num2 = -(num2)
    somma = num1
    while n < num2:
        somma = somma + num1
        n += 1
elif num1 < 0 and num2 >= 0:
    num1 = -(num1)
    somma = num1
    while n < num2:
        somma = somma + num1
        n += 1
elif num1 >=0 and num2 < 0:
    num2 = -(num2)
    somma = num1
    while n < num2:
        somma = somma + num1
        n += 1
else:
    somma = num1
    while n < num2:
        somma = somma + num1
        n += 1
print(somma)
