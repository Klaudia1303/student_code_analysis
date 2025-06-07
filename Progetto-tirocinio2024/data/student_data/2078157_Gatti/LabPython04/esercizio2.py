n = input('inserisci un intero (* per terminare): ')
i = 0
while n != '*':
    if int(n) > 0:
        i += 1
    n = input('inserisci un intero (* per terminare): ')
print(i)
