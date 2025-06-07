s=input('stringa con minimo 2 caratteri e un numero')
l=0
nu=0
for i in range(len(s)):
    c=s[i]
    if c.isalpha():
        l+=1
    elif c.isdigit():
        nu+=1
        n=int(c)
if l>1 and nu==1:     
    for i in range(len(s)-n):
        if s[i]==s[i+n]:
            l=0
if l==0:
    print('True')
else:
    print('False')
