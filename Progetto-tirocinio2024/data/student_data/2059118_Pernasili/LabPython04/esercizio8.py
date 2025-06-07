finito = False
ps = input("Inserisci una stringa: ")
uchar = ps[len(ps)-1]
while not finito:
    s = input("Inserisci una stringa: ")
    pchar = s[0]
    if uchar == pchar:
        print(ps,s)
        finito = True
    else:
        ps = s
        uchar = s[len(s)-1]
