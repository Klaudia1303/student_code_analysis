s=str(input('Inserisci stringa '))
for i in range(len(s)):
    if s[i]!=s[-i-1]:
        break
if s[i]==s[len(s)-1]:
    print(i+1)
else:
    print(i)
