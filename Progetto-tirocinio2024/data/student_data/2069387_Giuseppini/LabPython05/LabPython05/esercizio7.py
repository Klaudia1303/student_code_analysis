s=input('inserisic una stringa: ')
c=False

for i in range(0,len(s)):
    if s.count(s[i:i+1])>1:
        c=True
        print(True)
        break
if not c:
    print(c)
