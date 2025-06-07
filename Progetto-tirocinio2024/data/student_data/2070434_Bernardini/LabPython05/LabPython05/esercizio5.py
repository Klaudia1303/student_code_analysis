s=input('inserire stringa: ')
n=int(input('inserire numero: '))
for i in range (0,len(s)-2):
    if s[i]!=s[i+n]:
        continue
    elif s[i]==s[i+n]:
        print('True')
        break
if s[i]!=s[i+n]:
    print('False')


