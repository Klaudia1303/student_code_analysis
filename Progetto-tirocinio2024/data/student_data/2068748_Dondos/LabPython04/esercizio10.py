same_len = False
s1 = input('Inserisci una stringa: ')
s2 = input('Inserisci una stringa: ')
somma = len(s1) + len(s2)

while not same_len:
    s = input('Inserisci una stringa: ')
    if somma==len(s):
        print(s1,s2,s, sep=' ')
        same_len = True
    else:
        s1 = s2
        s2 = s
        somma = len(s2) + len(s)
