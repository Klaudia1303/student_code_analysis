n = int(input('inserisci un intero positivo: '))
i = 0
tot = 1
while i < n:
    if n == 0 or n == 1:
        tot = 1
    else:
        tot = tot * (n - i)
    i += 1
print(tot)
