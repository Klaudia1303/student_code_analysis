i = 0
t = input('Inserisci una stringa: ')
while i < 1:
    y = t[-1]
    s = input('Inserisci una stringa: ')
    x = s[0]
    if x == y:
        i += 1
    else:
        t = s
print(t, s)
