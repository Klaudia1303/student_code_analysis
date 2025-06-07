s= input('immettere una stringa: ')
t=str(s)
for i in range(len(s)):
    x=int(t.count(s[i]))
    if x>=2:
        print('True')
        break
else:
    print('False')

