k=True
while k:
    s=str(input('Stringa '))
    n=int(input('Intero '))
    if len(s)>=2:
        k=False
    else:
        print('Stringa troppo piccola')
d=False
for i in range(len(s)//2):
    if s[i]==s[i+n]:
        d=True
if d:
    print('True')
else:
    print('False')
