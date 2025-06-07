x = int(input('inserisci un intero compreso tra 0 e 10: '))
y = int(input('inserisci un intero compreso tra 0 e 10: '))
i = 0
if 0<=x<=10 and 0<=y<=10:
    while i<=10:
        if i == x:
            i += 1
        if i == y:
            i += 1
        print(i)
        i += 1

