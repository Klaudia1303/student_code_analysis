s = input('Inserire stringa: ')
i = 0
l = len(s)
n = 0
while i < l:
    c = s.count(s[i])
    if c >= n:
        n = c
        le = s[i]
    i += 1
print (le)
    
