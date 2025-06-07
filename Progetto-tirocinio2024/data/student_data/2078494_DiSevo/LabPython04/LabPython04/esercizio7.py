s = input('Inserisci una stringa: ')
c = 0
r = 0
n = 0
while c < len(s):
    k = s[c]
    r = s.count(k)
    if r >= n:
        n = r
        M = k
    c +=1
print(M)

    
