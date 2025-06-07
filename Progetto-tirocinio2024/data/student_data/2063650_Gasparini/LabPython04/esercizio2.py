positivi = 0
while True:
    n = input("Numero: ")
    if n == "*":
        break
    elif int(n) > 0:
        positivi += 1
print(positivi)
