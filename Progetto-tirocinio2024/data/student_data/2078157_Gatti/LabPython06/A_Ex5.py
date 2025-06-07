s = input('inserisci una stringa alfanumerica: ')
massimo = 1
a = 0
j = 0
for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            j += 1
            if j >= massimo:
                massimo = j
                a = s[i]
        else:
            j = 1
            
            
print(a, massimo)
