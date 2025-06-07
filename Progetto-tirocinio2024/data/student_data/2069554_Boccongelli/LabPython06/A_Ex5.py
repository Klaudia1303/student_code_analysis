s = input('Inserisci una stringa: ')

m = ''
o = 0
for i in range(len(s)):
    t = 0
    for j in range(i, len(s)):
        if (s[j] != s[i]):
            break
        t += 1
    if (t >= o):
        m = s[i]
        o = t
print(m, o)
