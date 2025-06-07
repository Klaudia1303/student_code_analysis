s=input('Inserire stringa:')
for c in range(len(s)):
    if s.find(s[c])!=s.rfind(s[c]):
         print('True')
         break
if s.find(s[c])==s.rfind(s[c]):
    print('False')

        

