s, t ,u = input('Inserisci stringa: '),input('Inserisci stringa: '), input('Inserisci stringa: ')

while len(u) != len(s) + len(t):
    s = t
    t = u
    u = input('Inserisci stringa: ')
print(s, t, u)
