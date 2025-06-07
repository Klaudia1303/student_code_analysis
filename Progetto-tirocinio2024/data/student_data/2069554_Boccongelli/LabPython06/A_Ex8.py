s1 = input('Inserisci una stringa: ')
s2 = input('Inserisci una stringa: ')
n = int(input('Inserisci un intero: '))

s = ''
for i in range(len(s1)):
    if s2.count(s1[i]) != 0:
        if i - s2.find(s1[i]) <= n or i + s2.find(s1[i]) <= n:
            s += s1[i]
print(s)
