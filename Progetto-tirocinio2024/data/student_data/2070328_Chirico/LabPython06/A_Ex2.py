s = input('stringa = ')

a = 0
b = len(s)-1
livello = 0
for i in range (len(s)):
         if s[a] == s[b]:
                a = a+1
                b = b-1
                livello = livello+1
         else:
            break

print(livello)
