s=input('inserisci una stringa: ')
c=0
j=len(s)-1
for i in range(0,len(s)):
    if s[i]==s[j]:
        c+=1
    j-=1
if c==len(s):
    print('parola palindroma')
else:
    print(c//2)
