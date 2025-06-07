same = False
s = input('Inserisci una stringa: ')
sf = s[len(s)-1]
while not same:
    s1 = input('Inserisci una stringa: ')
    si = s1[0]
    if sf == si:
        print(s, s1)
        same = True
    else:
        s = s1
        sf = s1[len(s1)-1]
