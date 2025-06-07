n = int(input('Inserisci un intero positivo: '))
i = 0
F1 = 0
F2 = 1

while i < n:
    if i == 1:
        Fn = i
    else:
        Fn = F1 + F2
        F1 = F2
        F2 = Fn
    print(Fn)
    i += 1
