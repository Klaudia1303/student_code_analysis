s= input('stringa: ')
livello=0
for i in range(0,len(s)):
    if s[i] == s[-(i+1)]:
        livello = livello + 1
    else:
        break
print('palindroma di livello:', livello)
