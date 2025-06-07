s = input('inserisci stringa :')
f = input('inserisci stringa :')
while True:
    if s[len(s)-1] == f[0]:
        break
    s = f
    f = input('inserisci stringa :')
print(s , ' ' + f)
