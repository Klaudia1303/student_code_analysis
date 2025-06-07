s1 = input('Inserisci una stringa: ')
s2 = input('Inserisci una stringa: ')

car = ''
for i in range(len(s1)):
    if (s2.find(s1[i]) != -1):
        p = ''
        for j in range(len(s2)):
            if (s1[i] == s2[j]):
                t = ''
                for k in range(len(s2)):
                    if (i + k < len(s1) and j + k < len(s2)):
                        if (s1[i + k] != s2[j + k]):
                            break
                        t += s1[i + k]
                if (len(t) >= len(p)):
                    p = t
        if (len(p) >= len(car)):
            car = p
print(car)
