n = int(input('Inserisci un intero: '))

c = 1
cc = 0
i = 0
while i < n:
    if (i == 0):
        print(1)
    else:
        print(cc + c)
        temp = c
        c = cc + c
        cc = temp
    i += 1
