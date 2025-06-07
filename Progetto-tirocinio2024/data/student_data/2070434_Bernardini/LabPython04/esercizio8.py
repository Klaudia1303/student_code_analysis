finito= False
prs = input("Inserire una stringa: ")
lchar = prs[len(prs)-1]
while not finito:
    s = input("Inserire una stringa: ")
    fchar = s[0]
    if lchar == fchar:
        print(prs, s)
        same = True
    else:
        prs = s
        lchar = s[len(s)-1]
