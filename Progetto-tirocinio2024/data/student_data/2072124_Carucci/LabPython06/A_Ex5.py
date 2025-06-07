s  = input('Inserire una stringa non vuota: ')

occ = 1
maxocc = 0
c = ''
for i in range(1, len(s)):
    if s[i]==s[i-1] :
        occ += 1
    else:
        occ = 1
    if occ>=maxocc:
        maxocc = occ
        c = s[i]
print(c, maxocc)
        
