s = input('inserisci stringa:')
n = int(input('inserisci numero:'))
k = False
for i in range(0,len(s)):
    if n + 1 < len(s):
        if s[i] == s[n + 1]:
            k = True
print(k)
                   
