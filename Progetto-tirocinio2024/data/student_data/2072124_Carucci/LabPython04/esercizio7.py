s = input('Inserire un stringa non vuota: ')

c = ''
nmax = 0
i = 0

while i<len(s):
    n = s.count(s[i])
    if n>=nmax:
        nmax = n
        c = s[i]
    i+=1
print(c)
        
