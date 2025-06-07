sp = ''
spp = ''
finito = False
while not finito:
    s = input('Inserisci una stringa: ')
    if (len(sp) + len(spp) == len(s)):
        finito = True
        print(spp, sp, s)
    spp = sp
    sp = s
