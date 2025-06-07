same = False
prs = input("Inserire stringa: ")
lchar = prs[len(prs)-1]
while not same:
    s = input("Inserire stringa: ")
    fchar = s[0]
    if lchar == fchar:
        print(prs, s)
        same = True
    else:
        prs = s
        lchar = s[len(s)-1]
