s=input('inserire la stringa ')
lvl=0
for i in range(len(s)//2):
    if s[i]==s[len(s)-i-1]:
        lvl=lvl+1
if lvl==len(s)//2:
    print('palindromo')
else:
    print('livello',lvl)
