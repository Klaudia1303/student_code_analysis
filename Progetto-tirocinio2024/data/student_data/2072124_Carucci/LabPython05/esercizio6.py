s = input('Inserire una stringa: ')

lmax = 0

for i in range(len(s)):
    j = s.rfind(s[i])
    if (j-i)>lmax:
        lmax = j-i
print(lmax)
