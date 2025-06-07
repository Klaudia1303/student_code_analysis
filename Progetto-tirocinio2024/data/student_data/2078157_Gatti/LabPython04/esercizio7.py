s = input('inserisci una stringa non vuota: ')
i = 0
massimo = 0
c = 'a'
if s != '':
    while i < len(s):
        if s.count(s[i]) >= massimo:
            massimo = s.count(s[i])
            c = s[i]
        i += 1
print(c)
