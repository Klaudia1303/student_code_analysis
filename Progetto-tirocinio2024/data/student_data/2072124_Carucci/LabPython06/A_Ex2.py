s = input('Inserire un stringa: ')

for i in range(len(s)):
    if s[i]!=s[-i-1]:
        break
    

if (i+1)==len(s):
    print('La stringa è palindroma')
else:
    print('Il livello massimo di palindromicità della stringa è', i)
