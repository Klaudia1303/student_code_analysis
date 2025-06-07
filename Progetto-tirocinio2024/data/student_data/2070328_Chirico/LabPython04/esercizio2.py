#trova tutti i numeri interi positivi

n = input("intero n = ")
positivi = 0

while n != '*':
    if int(n) > 0:
        positivi = positivi +1
    n = input("prossimo = ")

print(positivi)
        
