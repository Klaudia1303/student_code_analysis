s = str(input('Insert string: '))
for i in range(len(s)):
    x = s[i]
if s.find(x)!=s.rfind(x):
    print('True')
else:
    print('False')
