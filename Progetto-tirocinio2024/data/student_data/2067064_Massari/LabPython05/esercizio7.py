s=input('inserire una stringa: ')
contatore=0
for i in range(len(s)):
    parola=s.count(s[i])
    if parola>1:
        contatore+=1
if contatore>=1:
    print('True')
else:
    print('False')
    