#trova quanti interi sono divisibili per 3

n = input("intero n = ")
divisibili = 0

while n != '0':
    if int(n)%3 == 0:
        divisibili = divisibili+int(n)
    n = input("prossimo = ")

print(divisibili)
