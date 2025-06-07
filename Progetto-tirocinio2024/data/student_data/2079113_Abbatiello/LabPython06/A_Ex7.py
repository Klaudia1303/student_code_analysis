s1 = input('inserisci stringa :')
s2 = input('inserisci stringa :')

a = ''
b = ''

for i in range(len(s1)):
    for j in range(len(s2)):
        if s[1] == s[2]:
            b = ''
            for x in range(len(s2) - j):
                if s1[i + x] == s2[j + x]:
                    b += s1[i + x]
                if len(b) > len(a):
                    a = b
print(a)
