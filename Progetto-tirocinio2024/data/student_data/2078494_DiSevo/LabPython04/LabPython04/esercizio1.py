ac = True
k = 0
while ac:
    s = input('Inserisci una stringa: ')
    if s.count('a') > 0 and s.count('c') > 0:
        ac = False
    k += 1
print(k)
