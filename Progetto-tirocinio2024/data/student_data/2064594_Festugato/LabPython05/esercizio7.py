s = input('inserisci una stringa: ')
volte= 0

for i in range(0,len(s)+1):
    for c in range(i+1,len(s)):
        if s[i]==s[c]:
            volte += 1
if volte>=1:
    print('True')
else:
    print('False')
        
