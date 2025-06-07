s=str(input('Stringa '))
d=False
for n in range(len(s)):
    for i in range(len(s)):
        if s[n]==s[i] and n!=i:
            d=True
if d:
    print('True')
else:
    print('False')
      
