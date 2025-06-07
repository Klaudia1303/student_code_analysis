s = input('Inserisci una stringa: ')
t = input('Inserisci una stringa: ')
u = ''
if len(s)==len(t):
    for i in range(len(s)):
        u = u + s[i] + t[i]
print(u)
